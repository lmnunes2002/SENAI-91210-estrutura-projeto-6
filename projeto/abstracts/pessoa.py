from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    # Construtor
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__()
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    # Método abstrato.
    @abstractmethod
    def apresentar(self):
        pass

    # Similar ao ToString.
    def __str__(self) -> str:
        return (
            f"super().__str__()"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição estadual: {self.inscricao_estadual}"
            )