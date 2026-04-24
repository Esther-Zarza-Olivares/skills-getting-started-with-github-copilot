"""
Integration tests for the FastAPI application.
"""


def test_signup_then_unregister_flow(client, reset_activities):
    # Arrange
    email = "integration@mergington.edu"
    activity_name = "Drama Club"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    after_signup = client.get("/activities")

    unregister_response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    after_unregister = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert email in after_signup.json()[activity_name]["participants"]
    assert unregister_response.status_code == 200
    assert email not in after_unregister.json()[activity_name]["participants"]
