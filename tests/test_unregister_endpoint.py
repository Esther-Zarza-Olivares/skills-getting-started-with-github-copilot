"""
Tests for the unregister endpoint (DELETE /activities/{activity_name}/signup)
"""


def test_successful_unregister(client, reset_activities):
    # Arrange
    email = "michael@mergington.edu"
    activity_name = "Chess Club"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity_name}"


def test_unregister_removes_student(client, reset_activities):
    # Arrange
    email = "michael@mergington.edu"
    activity_name = "Chess Club"

    # Act
    client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    response = client.get("/activities")

    # Assert
    assert email not in response.json()[activity_name]["participants"]


def test_unregister_student_not_registered(client, reset_activities):
    # Arrange
    email = "notregistered@mergington.edu"
    activity_name = "Chess Club"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"
