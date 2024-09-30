import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadefederativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua das Flores", 20, "Apartamento 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA.nome)
    return endereco

def test_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
        Endereco(20, 20, "Apartamento 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA.nome)

def test_pessoa_nome_vazio_retorna_mensagem():
    with pytest.raises(TypeError, match="O logradouro não pode estar vazio."):
        Endereco("", 20, "Apartamento 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA.nome)

def test_numero_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="Deve constar numeração"):
        Endereco("Rua das Flores", "", "Apartamento 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA.nome)

def test_endereco_numero_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O número não pode ser negativo"):
        Endereco("Rua das Flores", -20, "Apartamento 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA.nome)

def test_endereco_valido(endereco_valido):
    assert endereco_valido._logradouro == "Rua das Flores"
    assert endereco_valido._numero == 20
    assert endereco_valido._complemento == "Apartamento 45"
    assert endereco_valido._cep == "12345-678"
    assert endereco_valido._cidade == "Salvador"
    assert endereco_valido._uf == UnidadeFederativa.BAHIA.nome

def test_unidade_federativa_membros():
    assert UnidadeFederativa.BAHIA in UnidadeFederativa
    assert UnidadeFederativa.SAO_PAULO in UnidadeFederativa
    assert UnidadeFederativa.RIO_DE_JANEIRO in UnidadeFederativa

def test_unidade_federativa_valores_validos():
    assert UnidadeFederativa.BAHIA.nome == "Bahia"
    assert UnidadeFederativa.BAHIA.sigla == "BA"
    assert UnidadeFederativa.RIO_DE_JANEIRO.nome == "Rio de Janeiro"
    assert UnidadeFederativa.RIO_DE_JANEIRO.sigla == "RJ"
    assert UnidadeFederativa.SAO_PAULO.nome == "São Paulo"
    assert UnidadeFederativa.SAO_PAULO.sigla == "SP"