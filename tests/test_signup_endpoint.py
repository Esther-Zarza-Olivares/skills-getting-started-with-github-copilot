"""
Tests for the signup endpoint (POST /activities/{activity_name}/signup)
"""


def test_successful_signup(client, reset_activities):
    # Arrange
    email = "newstudent@mergington.edu"
    activity_name = "Chess Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"


def test_signup_adds_student_to_participants(client, reset_activities):
    # Arrange
    email = "newstudent@mergington.edu"
    activity_name = "Chess Club"

    # Act
    client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    response = client.get("/activities")

    # Assert
    assert email in response.json()[activity_name]["participants"]


def test_signup_duplicate_student(client, reset_activities):
    # Arrange
    email = "michael@mergington.edu"
    activity_name = "Chess Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_nonexistent_activity(client, reset_activities):
    # Arrange
    email = "student@mergington.edu"
    activity_name = "Nonexistent Activity"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
