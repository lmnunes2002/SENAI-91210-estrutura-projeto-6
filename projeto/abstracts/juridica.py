from abc import ABC, abstractmethod
from pessoa import Pessoa
from projeto.models.endereco import Endereco

class Juridica(ABC, Pessoa):
    # Método abstrato.
    @abstractmethod
    def apresentar(self):
        pass
    
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual