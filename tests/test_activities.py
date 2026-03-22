def test_get_all_activities(client):
    """Test retrieving all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    activity = data["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity

def test_activity_has_participants_list(client):
    """Test that activities include participant information"""
    response = client.get("/activities")
    data = response.json()
    for activity_name, activity in data.items():
        assert isinstance(activity["participants"], list)
        for email in activity["participants"]:
            assert "@" in email
