import sys
sys.path.append('.')
import time
import datetime
from dateutil import parser
from main import app
from fastapi.testclient import TestClient
client = TestClient(app)


def test_server_status():
    response = client.get("/")
    assert response.status_code == 200


def test_endpoints():
    response = client.get("/populate")
    assert response.status_code == 200

    response = client.get("/medals")
    assert response.status_code == 200

    response = client.get("/medals/2004")
    assert response.status_code == 200

    response = client.get("/results")
    assert response.status_code == 200

    response = client.get("/countries")
    assert response.status_code == 200
