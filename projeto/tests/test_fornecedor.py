import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.tests.test_endereco import endereco_valido

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(1, "Carlos Oliveira", "9876-5432", "carlos@example.com", endereco_valido, "12.345.678/0001-90", "12345678", "luz")
    return fornecedor

def test_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.id == 1
    assert fornecedor_valido.nome == "Carlos Oliveira"
    assert fornecedor_valido.telefone == "9876-5432"