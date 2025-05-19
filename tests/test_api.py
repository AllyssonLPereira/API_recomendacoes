import pytest
from fastapi.testclient import TestClient 
from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo à API de Recomendação de Produtos"}


def test_criar_protudos():
    reponse = client.post("/produtos/", json={
        "nome": "produto A",
        "categoria": "categoria 1",
        "tags": ["tag 1", "tag 2"],
    })

    assert reponse.status_code == 200
    assert reponse.json()["nome"] == "produto A"
    assert reponse.json()["categoria"] == "categoria 1"
    assert reponse.json()["tags"] == ["tag 1", "tag 2"]


def test_listar_produtos():
    response = client.get("/produtos/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_criar_usuarios():
    reponse = client.post("/usuarios/", params={"nome": "usuario 1"})
    usuario_data = reponse.json()

    assert reponse.status_code == 200
    assert usuario_data["nome"] == "usuario 1"
    assert usuario_data["id"] == 1


def test_listar_usuarios():
    response = client.get("/usuarios/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_criar_historico():
    response = client.post("/historico_compras/1", json = {
        "produtos_ids": [1]
    })

    assert response.status_code == 200
    assert response.json() == {"mensagem": "Histórico de compras atualizado"}


def test_recomendar_produtos():
    response = client.post("/recomendacoes/1", json = {
        "categorias": ["categoria 1"],
        "tags": ["tag 1"],
    })

    assert response.status_code == 200
    assert len(response.json()) == 1

