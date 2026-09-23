# CI/CD Test App

Aplicação simples de lista de tarefas usada como base para praticar pipelines de CI/CD.

- **Backend:** Python + FastAPI
- **Banco de dados:** SQLite (via SQLAlchemy)
- **Testes:** Pytest + TestClient (banco em memória, isolado dos testes)
- **Front-end:** HTML/CSS/JS puro, servido pelo próprio FastAPI (`static/index.html`)

## Estrutura

```
app/
  main.py          # instância do FastAPI, health check, monta o front-end
  database.py      # engine SQLite, sessão, dependency get_db
  models.py        # modelo SQLAlchemy (Task)
  schemas.py       # schemas Pydantic (entrada/saída)
  routers/
    tasks.py       # rotas CRUD de /api/tasks
static/
  index.html       # front-end que consome a API
tests/
  conftest.py      # fixture de client com banco em memória
  test_health.py
  test_tasks.py
requirements.txt
pytest.ini
```

## Rodando localmente

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Acesse `http://127.0.0.1:8000` para ver a interface, ou `http://127.0.0.1:8000/docs` para a documentação automática da API (Swagger).

## Rodando os testes

```bash
pytest
```

## Endpoints

| Método | Rota              | Descrição                |
|--------|-------------------|---------------------------|
| GET    | `/api/health`      | Health check              |
| GET    | `/api/tasks/`      | Lista as tarefas          |
| POST   | `/api/tasks/`      | Cria uma tarefa           |
| PATCH  | `/api/tasks/{id}`  | Atualiza status (done)    |
| DELETE | `/api/tasks/{id}`  | Remove uma tarefa         |
