def test_unregister_student_successfully(client):
    email = "michael@mergington.edu"
    response = client.post(
        "/activities/Chess Club/unregister",
        params={"email": email}
    )
    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]
    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email not in participants

def test_unregister_not_registered_fails(client):
    response = client.post(
        "/activities/Chess Club/unregister",
        params={"email": "notregistered@mergington.edu"}
    )
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]

def test_unregister_nonexistent_activity(client):
    response = client.post(
        "/activities/Fake Activity/unregister",
        params={"email": "test@mergington.edu"}
    )
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

def test_signup_then_unregister_twice_fails(client):
    email = "test@mergington.edu"
    activity = "Basketball Team"
    client.post(f"/activities/{activity}/signup", params={"email": email})
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert response.status_code == 200
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert response.status_code == 400
