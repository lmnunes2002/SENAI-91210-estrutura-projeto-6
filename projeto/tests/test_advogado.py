import pytest
from projeto.models.advogado import Advogado
from projeto.tests.test_endereco import endereco_valido
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def advogado_valido():
    advogado = Advogado(1, "João Silva", "(11) 91234-5678", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "1985-05-20", "123.456.789-00", "12.345.678-9", "0123456789", Setor.JURIDICO, 8000.00, "SP 12345")
    return advogado

def test_oab_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O OAB deve ser alfa-numérico."):
       Advogado(1, "João Silva", "(11) 91234-5678", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "1985-05-20", "123.456.789-00", "12.345.678-9", "0123456789", Setor.JURIDICO, 8000.00, 123)

def test_oab_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O OAB não pode estar vazio."):
        Advogado(1, "João Silva", "(11) 91234-5678", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "1985-05-20", "123.456.789-00", "12.345.678-9", "0123456789", Setor.JURIDICO, 8000.00, "")

def test_oab_tam_mensagem():
    with pytest.raises(ValueError, match="O tamanho do OAB não pode ser diferente de 8 carácteres."):
        Advogado(1, "João Silva", "(11) 91234-5678", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "1985-05-20", "123.456.789-00", "12.345.678-9", "0123456789", Setor.JURIDICO, 8000.00, "SP 123456")

def test_advogado_valido(advogado_valido):
    assert advogado_valido.id == 1
    assert advogado_valido.nome == "João Silva"
    assert advogado_valido.telefone == "(11) 91234-5678"
    assert advogado_valido.email == "joao.silva@email.com"
    assert advogado_valido.endereco == endereco_valido
    assert advogado_valido.sexo == Sexo.MASCULINO
    assert advogado_valido.estado_civil == EstadoCivil.CASADO
    assert advogado_valido.data_nascimento == "1985-05-20"
    assert advogado_valido.cpf == "123.456.789-00"
    assert advogado_valido.rg == "12.345.678-9"
    assert advogado_valido.matricula == "0123456789"
    assert advogado_valido.setor == Setor.JURIDICO
    assert advogado_valido.salario == 8000.00
    assert advogado_valido.oab == "SP 12345"

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