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