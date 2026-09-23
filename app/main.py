from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import models
from .database import engine
from .routers import tasks

# Cria as tabelas no SQLite caso ainda não existam.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CI/CD Test App", version="1.0.0")

app.include_router(tasks.router)


@app.get("/api/health", tags=["health"])
def health_check():
    return {"status": "ok"}


# Serve o front-end estático (static/index.html) na raiz "/".
# Registrado por último para não sobrepor as rotas /api/*.
app.mount("/", StaticFiles(directory="static", html=True), name="static")
