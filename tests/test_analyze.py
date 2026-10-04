from fastapi.testclient import TestClient
from collect.main import app

client = TestClient(app)


def test_summary():
    payload = client.post("/analyze", json={"rows": [{'endpoint': '/healthz', 'latency_ms': 40}, {'endpoint': '/healthz', 'latency_ms': 200}, {'endpoint': '/ready', 'latency_ms': 120}]}).json()
    assert payload["mean"] == 120.0
    assert payload["by_endpoint"]["/healthz"]


def test_empty_is_refused():
    assert client.post("/analyze", json={"rows": []}).status_code == 422
