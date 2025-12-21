"""
Fixtures compartilhadas para testes.

Este arquivo é carregado automaticamente pelo pytest e suas fixtures
ficam disponíveis para todos os testes.
"""
import pytest
from fastapi.testclient import TestClient
from template import app
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def client():
    return TestClient(app)
