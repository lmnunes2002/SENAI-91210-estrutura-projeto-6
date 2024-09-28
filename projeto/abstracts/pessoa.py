from abc import ABC, abstractmethod
from models.endereco import Endereco

class Pessoa(ABC):
    # Método abstrato.
    @abstractmethod
    def apresentar(self):
        pass

    # Construtor
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__()
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    # Similar ao ToString.
    def __str__(self) -> str:
        return (
            "super().__str__()"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição estadual: {self.inscricao_estadual}"
            )