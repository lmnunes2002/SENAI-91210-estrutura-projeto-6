import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.tests.test_endereco import endereco_valido
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro(1, "João da Silva", "1234-5678", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "01/01/1980", "123.456.789-00", "12.345.678-9", "1234567890", Setor.ENGENHARIA, 8000.0, "123456/PR")
    return engenheiro

def test_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.id == 1
    assert engenheiro_valido.nome == "João da Silva"
    assert engenheiro_valido.telefone == "1234-5678"
    assert engenheiro_valido.email == "joao.silva@email.com"
    assert engenheiro_valido.endereco == endereco_valido
    assert engenheiro_valido.sexo == Sexo.MASCULINO
    assert engenheiro_valido.estado_civil == EstadoCivil.CASADO
    assert engenheiro_valido.data_nascimento == "01/01/1980"
    assert engenheiro_valido.cpf == "123.456.789-00"
    assert engenheiro_valido.rg == "12.345.678-9"
    assert engenheiro_valido.matricula == "1234567890"
    assert engenheiro_valido.setor == Setor.ENGENHARIA
    assert engenheiro_valido.salario == 8000.0
    assert engenheiro_valido.crea == "123456/PR"

def test_setor_membros():
    assert Setor.ENGENHARIA in Setor
    assert Setor.JURIDICO in Setor
    assert Setor.SAUDE in Setor

def test_setor_valores_validos():
    assert Setor.ENGENHARIA.texto == "Engenharia"
    assert Setor.JURIDICO.texto == "Jurídico"
    assert Setor.SAUDE.texto == "Saúde"