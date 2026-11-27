
import os
import sys
import uuid

sys.path.insert(0, os.path.abspath("application"))

from app import app


def test_homepage():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_add_student():
    client = app.test_client()
    email = f"test-{uuid.uuid4().hex}@example.com"

    response = client.post("/add", data={
        "name": "Test Student",
        "email": email,
        "course": "Computer Science"
    })

    assert response.status_code == 302


def test_invalid_student():
    client = app.test_client()
    response = client.post("/add", data={
        "name": "",
        "email": "",
        "course": ""
    })

    assert response.status_code == 400
