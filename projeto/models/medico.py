from projeto.abstracts.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crm: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento, cpf, rg, matricula, setor, salario)
        self.crm = self._verificar_crm(crm)

    # Método de verificação
    def _verificar_crm(self, valor):
        """Método para verificar CRM"""
        self.__verificar_crm_invalido(valor)
        self.__verificar_crm_vazio(valor)
        self.__verificar_crm_tam(valor)

        self.crea = valor
        return valor
    
    # Método auxiliar
    def __verificar_crm_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CRM deve ser alfa-numérico.")
        
    # Método auxiliar.
    def __verificar_crm_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O CRM não pode estar vazio.")
        
    # Método auxiliar.
    def __verificar_crm_tam(self, valor):
        if len(valor) != 12:
            raise ValueError("O tamanho do CRM não pode ser diferente de 12 caractéres.")

    # Instanciando método abstrato.    
    def apresentar(self):
        return (
            f"Nome: {self.nome}"
        )