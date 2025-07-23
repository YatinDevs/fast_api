def test_read_main(test_client):
    response = test_client.get("/api/v1/test")
    assert response.status_code == 200
    assert "API is running" in response.text

def test_404_response(test_client):
    response = test_client.get("/non-existent-route")
    assert response.status_code == 404