from abc import abstractmethod
from projeto.abstracts.pessoa import Pessoa
from projeto.models.endereco import Endereco

class Juridica(Pessoa):
    # Construtor
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

    # Método abstrato.
    @abstractmethod
    def apresentar(self):
        pass

    # Similar ao ToString.
    def __str__(self) -> str:
        return (
            f"super().__str__()"
            f"CNPJ: {self.cnpj}"
            f"Inscrição estadual: {self.inscricao_estadual}"
            )