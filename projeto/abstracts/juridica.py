from abc import abstractmethod
from projeto.abstracts.pessoa import Pessoa
from projeto.models.endereco import Endereco

class Juridica(Pessoa):
    # Construtor
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricao_estadual = self._verificar_inscricao_estadual(inscricao_estadual)

    # Método abstrato.
    @abstractmethod
    def apresentar(self):
        pass
    
    # Método para verificação.
    def _verificar_cnpj(self, valor):
        """Método para verificação do CNPJ"""
        self.__verificar_cnpj_vazio(valor)

        self.cnpj = valor
        return self.cnpj
        
    # Método auxiliar.
    def __verificar_cnpj_vazio(self, valor):
        """Método auxiliar para verificar CNPJ's vazios"""
        if not valor.strip():
            raise ValueError("O CNPJ não pode estar vazio.")
        
    # Método para verificação.
    def _verificar_inscricao_estadual(self, valor):
        """Método para verificação de Inscrição Estadual"""
        self.__verificar_inscricao_estadual_vazio(valor)

        self.inscricao_estadual = valor
        return self.inscricao_estadual
        
    # Método auxiliar.
    def __verificar_inscricao_estadual_vazio(self, valor):
        """Método auxiliar para verificar Inscrições vazias"""
        if not valor.strip():
            raise ValueError("A inscrição estadual não pode estar vazia.")
        
    # Similar ao ToString.
    def __str__(self) -> str:
        return (
            f"super().__str__()"
            f"CNPJ: {self.cnpj}"
            f"Inscrição estadual: {self.inscricao_estadual}"
            )