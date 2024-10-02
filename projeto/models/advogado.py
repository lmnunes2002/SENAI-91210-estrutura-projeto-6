from projeto.abstracts.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, oab: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento, cpf, rg, matricula, setor, salario)
        self.oab = self._verificar_oab(oab)

    # Método de verificação
    def _verificar_oab(self, valor):
        """Método para verificar OAB"""
        self.__verificar_oab_invalido(valor)
        self.__verificar_oab_vazio(valor)
        self.__verificar_oab_tam(valor)

        self.oab = valor
        return valor
    
    # Método auxiliar
    def __verificar_oab_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O OAB deve ser alfa-numérico.")
        
    # Método auxiliar.
    def __verificar_oab_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O OAB não pode estar vazio.")
        
    # Método auxiliar.
    def __verificar_oab_tam(self, valor):
        if len(valor) != 8:
            raise ValueError("O tamanho do OAB não pode ser diferente de 8 carácteres.")
        
    # Instanciando método abstrato.    
    def apresentar(self):
        return (
            f"Nome: {self.nome}"
        )