import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.tests.test_endereco import endereco_valido

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(1, "Carlos Oliveira", "9876-5432", "carlos@email.com", endereco_valido, "12.345.678/0001-90", "12345678", "frutas")
    return fornecedor

def test_id_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O ID deve ser um número."):
        Fornecedor("a", "Carlos Oliveira", "9876-5432", "carlos@email.com", endereco_valido, "12.345.678/0001-90", "12345678", "frutas")

def test_id_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O ID não pode ser negativo."):
        Fornecedor(-1, "Carlos Oliveira", "9876-5432", "carlos@email.com", endereco_valido, "12.345.678/0001-90", "12345678", "frutas")

def test_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Fornecedor(1, 2, "9876-5432", "carlos@email.com", endereco_valido, "12.345.678/0001-90", "12345678", "frutas")

def test_nome_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O nome não pode estar vazio."):
        Fornecedor(1, "", "9876-5432", "carlos@email.com", endereco_valido, "12.345.678/0001-90", "12345678", "frutas")

def test_inscricao_estadual_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="A inscrição estadual não pode estar vazia."):
        Fornecedor(1, "Carlos Oliveira", "9876-5432", "carlos@email.com", endereco_valido, "12.345.678/0001-90", "", "frutas")

def test_cnpj_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O CNPJ não pode estar vazio."):
        Fornecedor(1, "Carlos Oliveira", "9876-5432", "carlos@email.com", endereco_valido, "", "12345678", "frutas")

def test_produto_tipo_invalido_retorna_mesnagem():
    with pytest.raises(TypeError, match="O produto deve ser um texto"):
        Fornecedor(1, "Carlos Oliveira", "9876-5432", "carlos@email.com", endereco_valido, "12.345.678/0001-90", "12345678", 2)

def test_inscricao_estadual_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O produto não pode estar vazio"):
        Fornecedor(1, "Carlos Oliveira", "9876-5432", "carlos@email.com", endereco_valido, "12.345.678/0001-90", "12345678", "")

def test_fornecedor_valido(fornecedor_valido):
    assert fornecedor_valido.id == 1
    assert fornecedor_valido.nome == "Carlos Oliveira"
    assert fornecedor_valido.telefone == "9876-5432"
    assert fornecedor_valido.email == "carlos@email.com"
    assert fornecedor_valido.endereco == endereco_valido
    assert fornecedor_valido.cnpj == "12.345.678/0001-90"
    assert fornecedor_valido.inscricao_estadual == "12345678"
    assert fornecedor_valido.produto == "frutas"