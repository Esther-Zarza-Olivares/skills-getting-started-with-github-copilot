"""
Tests for the activities endpoint (GET /activities)
"""


def test_get_all_activities(client, reset_activities):
    # Arrange / Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    expected_activities = [
        "Chess Club", "Programming Class", "Gym Class",
        "Basketball Team", "Tennis Club", "Art Studio",
        "Drama Club", "Debate Team", "Science Club"
    ]
    assert all(activity in data for activity in expected_activities)


def test_activities_structure(client, reset_activities):
    # Arrange / Act
    response = client.get("/activities")
    activity = response.json()["Chess Club"]

    # Assert
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)
    assert isinstance(activity["max_participants"], int)


def test_activity_participants_content(client, reset_activities):
    # Arrange / Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in data["Chess Club"]["participants"]
