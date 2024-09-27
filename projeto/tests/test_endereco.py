import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadefederativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua das Flores", "vinte", "Apartamento 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA.nome)
    return endereco

def test_endereco_logradouro_valido(endereco_valido):
    assert endereco_valido._logradouro == "Rua das Flores"