import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.api.endpoints.hashtags_router import router as hashtags_router, read_csv_data
from backend.api.endpoints.hashtags_router import CSV_FILE_PATH

client = TestClient(app)

def test_get_top_hashtags():
    response = client.get("/top_hashtags?start_date=2024-02-01%2000:00:00&end_date=2024-02-02%2000:00:00")
    assert response.status_code == 200
    assert "top_hashtags" in response.json()

def test_invalid_date_range():
    response = client.get("/top_hashtags?start_date=2024-02-01&end_date=2024-02-02")
    assert response.status_code == 422
    assert "validation error" in response.json()["detail"][0]["msg"]

def test_csv_data_loading():
    data = read_csv_data(CSV_FILE_PATH)
    assert isinstance(data, list)
    assert len(data) > 0
