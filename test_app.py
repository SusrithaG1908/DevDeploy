"""
Unit tests for the Student Management System.
Run with: pytest -v
"""

import pytest
import app as app_module
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Management System" in response.data


def test_home_lists_existing_students(client):
    response = client.get("/")
    assert b"Susritha" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_api_students(client):
    response = client.get("/api/students")
    assert response.status_code == 200
    data = response.get_json()
    assert "students" in data
    assert len(data["students"]) >= 3


def test_add_student(client):
    before = len(app_module.students)
    response = client.post(
        "/add",
        data={"name": "Test Student", "branch": "CSE", "year": "2"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert len(app_module.students) == before + 1
    assert b"Test Student" in response.data


def test_delete_student(client):
    client.post("/add", data={"name": "ToDelete", "branch": "IT", "year": "1"})
    target = next(s for s in app_module.students if s["name"] == "ToDelete")
    before = len(app_module.students)
    response = client.post(f"/delete/{target['id']}", follow_redirects=True)
    assert response.status_code == 200
    assert len(app_module.students) == before - 1
