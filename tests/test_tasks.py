def test_list_tasks_empty(client):
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_task(client):
    response = client.post("/api/tasks/", json={"title": "Estudar CI/CD"})
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Estudar CI/CD"
    assert data["done"] is False
    assert "id" in data


def test_list_tasks_after_create(client):
    client.post("/api/tasks/", json={"title": "Configurar pipeline"})
    client.post("/api/tasks/", json={"title": "Rodar pytest"})

    response = client.get("/api/tasks/")
    assert response.status_code == 200

    titles = [task["title"] for task in response.json()]
    assert titles == ["Configurar pipeline", "Rodar pytest"]


def test_update_task_done(client):
    created = client.post("/api/tasks/", json={"title": "Marcar como feita"})
    task_id = created.json()["id"]

    response = client.patch(f"/api/tasks/{task_id}", json={"done": True})
    assert response.status_code == 200
    assert response.json()["done"] is True


def test_update_task_not_found(client):
    response = client.patch("/api/tasks/999", json={"done": True})
    assert response.status_code == 404


def test_delete_task(client):
    created = client.post("/api/tasks/", json={"title": "Remover depois"})
    task_id = created.json()["id"]

    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 204

    response = client.get("/api/tasks/")
    assert response.json() == []


def test_delete_task_not_found(client):
    response = client.delete("/api/tasks/999")
    assert response.status_code == 404
