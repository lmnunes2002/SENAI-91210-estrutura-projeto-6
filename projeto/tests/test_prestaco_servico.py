import pytest
from projeto.models.prestacao_servico import PrestacaoServico
from projeto.tests.test_endereco import endereco_valido

@pytest.fixture
def prestacao_servico_valido():
    prestacao_servico = PrestacaoServico(1, "Serviço Exemplo", "123456789", "exemplo@email.com", endereco_valido, "12.345.678/0001-99", "123456789", "2024-01-01", "2024-12-31")
    return prestacao_servico

def test_contrato_inicio_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O inicio de contrato deve ser alfa-númerico."):
        PrestacaoServico(1, "Serviço Exemplo", "123456789", "exemplo@email.com", endereco_valido, "12.345.678/0001-99", "123456789", 123, "2024-12-31")

def test_contrato_inicio_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O início do contrato não pode estar vazio."):
        PrestacaoServico(1, "Serviço Exemplo", "123456789", "exemplo@email.com", endereco_valido, "12.345.678/0001-99", "123456789", "", "2024-12-31")

def test_contrato_fim_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O final do contrato deve ser alfa-númerico."):
        PrestacaoServico(1, "Serviço Exemplo", "123456789", "exemplo@email.com", endereco_valido, "12.345.678/0001-99", "123456789", "2024-01-01", 123)

def test_contrato_fim_vazio_retorna_mensagem(): 
    with pytest.raises(ValueError, match="O fim do contrato não pode estar vazio."):
        PrestacaoServico(1, "Serviço Exemplo", "123456789", "exemplo@email.com", endereco_valido, "12.345.678/0001-99", "123456789", "2024-01-01", "")