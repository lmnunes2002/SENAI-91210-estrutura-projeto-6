from projeto.abstracts.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str, protocolo_atendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento)
        self._protocolo_atendimento = self._verificar_protocolo_atendimento(protocolo_atendimento)

    # Método para verificação.
    def _verificar_protocolo_atendimento(self, valor):
        """Método para verificação do protocolo de atendimento"""
        self.__verificar_protocolo_atendimento_tipo_invalido(valor)
        self.__verificar_protocolo_atendimento_vazio(valor)
        self.__verificar_protocolo_atendimento_tam(valor)

        self.protocolo_atendimento = valor
        return valor
    
    # Método auxiliar. 
    def __verificar_protocolo_atendimento_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo do protocolo"""
        if not isinstance(valor, str):
            raise TypeError("O protocolo de atendimento deve ser um texto.")

    # Método auxiliar.     
    def __verificar_protocolo_atendimento_vazio(self, valor):
        """Método auxiliar para verificar protocolos vazios"""
        if not valor.strip():
            raise ValueError("O protocolo de atendimento não pode estar vazio.")

    # Método auxiliar.     
    def __verificar_protocolo_atendimento_tam(self, valor):
        """Método auxiliar para verificar tamanho de protocolo"""
        if len(valor) < 9:
            raise ValueError("O protocolo deve conter 9 caracteres.")
        
    # Instanciando método abstrato.    
    def apresentar(self):
        return (
            f"Nome: {self.nome}"
        )    