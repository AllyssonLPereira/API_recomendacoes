from app.routers import routers_produtos, routers_usuarios
from fastapi import FastAPI
from typing import Dict


MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos"


# Criando o App
app = FastAPI()


app.include_router(routers_produtos.router)
app.include_router(routers_usuarios.router)


# Iniciando o servidor
@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}