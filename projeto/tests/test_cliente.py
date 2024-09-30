import pytest
from projeto.models.cliente import Cliente
from projeto.tests.test_endereco import endereco_valido
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def cliente_valido():
    cliente = Cliente(1, "João da Silva", "(11) 98765-4321", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "1990-01-01", "123456789")
    return cliente


def test_data_nascimento_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A data de nascimento deve ser númerica."):
        cliente = Cliente(1, "João da Silva", "(11) 98765-4321", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, True, "123456789")

def test_data_nascimento_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="A data de nascimento não pode estar vazia."):
        Cliente(1, "João da Silva", "(11) 98765-4321", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "", "123456789")

def test_protocolo_atendimento_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve ser um texto."):
        Cliente(1, "João da Silva", "(11) 98765-4321", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "1990-01-01", 123456789)

def test_protocolo_atendimento_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O protocolo de atendimento não pode estar vazio."):
        Cliente(1, "João da Silva", "(11) 98765-4321", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "1990-01-01", "")

def test_protocolo_atendimento_tam_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O protocolo deve conter 9 caracteres."):
        Cliente(1, "João da Silva", "(11) 98765-4321", "joao.silva@email.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "1990-01-01", "12345678")
    
def test_sexo_membros():
    assert Sexo.MASCULINO in Sexo
    assert Sexo.FEMININO in Sexo

def test_sexo_valores_validos():
    assert Sexo.MASCULINO.caractere == "M"
    assert Sexo.MASCULINO.texto == "Masculino"
    assert Sexo.FEMININO.caractere == "F"
    assert Sexo.FEMININO.texto == "Feminino"

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

# # Método para verificação.
#     def _verificar_protocolo_atendimento(self, valor):
#         """Método para verificação do protocolo de atendimento"""
#         self.__verificar_protocolo_atendimento_tipo_invalido(valor)
#         self.__verificar_protocolo_atendimento_vazio(valor)
#         self.__verificar_protocolo_atendimento_tam(valor)

#         self.protocolo_atendimento = valor
#         return valor
    
#     # Método auxiliar. 
#     def __verificar_protocolo_atendimento_tipo_invalido(self, valor):
#         """Método auxiliar para verificação de tipo do protocolo"""
#         if not isinstance(valor, str):
#             raise TypeError("O protocolo de atendimento deve ser um texto.")

#     # Método auxiliar.     
#     def __verificar_protocolo_atendimento_vazio(self, valor):
#         """Método auxiliar para verificar protocolos vazios"""
#         if not valor.strip():
#             raise ValueError("O protocolo de atendimento não pode estar vazio.")

#     # Método auxiliar.     
#     def __verificar_protocolo_atendimento_tam(self, valor):
#         """Método auxiliar para verificar tamanho de protocolo"""
#         tam = len(self._protocolo_atendimento)
#         if tam < 9:
#             raise ValueError("O protocolo deve conter 9 caracteres.")
        
