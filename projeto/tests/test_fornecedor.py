import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.tests.test_endereco import endereco_valido

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(1, "Carlos Oliveira", "9876-5432", "carlos@example.com", endereco_valido, "12.345.678/0001-90", "12345678")

def test_id_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O ID deve ser um número"):
        fornecedor = Fornecedor("a", "Carlos Oliveira", "9876-5432", "carlos@example.com", endereco_valido, "12.345.678/0001-90", "12345678")