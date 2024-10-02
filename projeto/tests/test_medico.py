import pytest
from projeto.models.medico import Medico
from projeto.tests.test_endereco import endereco_valido
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def medico_valido():
    medico = Medico(1, "Dr. João da Silva", "(11) 91234-5678", "joao.silva@exemplo.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "1980-05-15", "123.456.789-00", "12.345.678-9", "1234567890", Setor.SAUDE, 15000.00, "CRM-SP 12345")
    return medico

def test_crm_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O CRM deve ser alfa-numérico."):
        Medico(1, "Dr. João da Silva", "(11) 91234-5678", "joao.silva@exemplo.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "1980-05-15", "123.456.789-00", "12.345.678-9", "1234567890", Setor.SAUDE, 15000.00, 123)

def test_crm_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O CRM não pode estar vazio."):
        Medico(1, "Dr. João da Silva", "(11) 91234-5678", "joao.silva@exemplo.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "1980-05-15", "123.456.789-00", "12.345.678-9", "1234567890", Setor.SAUDE, 15000.00, "")

def test_medico_valido(medico_valido):
    assert medico_valido.id == 1
    assert medico_valido.nome == "Dr. João da Silva"
    assert medico_valido.telefone == "(11) 91234-5678"
    assert medico_valido.email == "joao.silva@exemplo.com"
    assert medico_valido.endereco == endereco_valido
    assert medico_valido.sexo == Sexo.MASCULINO
    assert medico_valido.estado_civil == EstadoCivil.CASADO
    assert medico_valido.data_nascimento == "1980-05-15"
    assert medico_valido.cpf == "123.456.789-00"
    assert medico_valido.rg == "12.345.678-9"
    assert medico_valido.matricula == "1234567890"
    assert medico_valido.setor == Setor.SAUDE
    assert medico_valido.salario == 15000.00
    assert medico_valido.crm == "CRM-SP 12345"

def test_setor_membros():
    assert Setor.ENGENHARIA in Setor
    assert Setor.JURIDICO in Setor
    assert Setor.SAUDE in Setor

def test_setor_valores_validos():
    assert Setor.ENGENHARIA.texto == "Engenharia"
    assert Setor.JURIDICO.texto == "Jurídico"
    assert Setor.SAUDE.texto == "Saúde"

def test_estado_civil_membros():
    assert EstadoCivil.SOLTEIRO in EstadoCivil
    assert EstadoCivil.CASADO in EstadoCivil
    assert EstadoCivil.SEPARADO in EstadoCivil
    assert EstadoCivil.DIVORCIADO in EstadoCivil
    assert EstadoCivil.VIUVO in EstadoCivil

def test_estado_civil_valores_validos():
    assert EstadoCivil.SOLTEIRO.texto == "Solteiro"
    assert EstadoCivil.CASADO.texto == "Casado"
    assert EstadoCivil.SEPARADO.texto == "Separado"
    assert EstadoCivil.DIVORCIADO.texto == "Divorciado"
    assert EstadoCivil.VIUVO.texto == "Viúvo"