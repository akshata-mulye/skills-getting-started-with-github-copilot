def test_signup_student_successfully(client):
    response = client.post(
        "/activities/Basketball Team/signup",
        params={"email": "alex@mergington.edu"}
    )
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    activities_response = client.get("/activities")
    participants = activities_response.json()["Basketball Team"]["participants"]
    assert "alex@mergington.edu" in participants

def test_signup_duplicate_fails(client):
    email = "michael@mergington.edu"
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": email}
    )
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]

def test_signup_nonexistent_activity(client):
    response = client.post(
        "/activities/Fake Activity/signup",
        params={"email": "test@mergington.edu"}
    )
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

def test_multiple_students_same_activity(client):
    activity = "Basketball Team"
    for email in ["alice@mergington.edu", "bob@mergington.edu", "charlie@mergington.edu"]:
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": email}
        )
        assert response.status_code == 200
    response = client.get("/activities")
    participants = response.json()[activity]["participants"]
    assert len(participants) == 3
