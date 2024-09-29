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

    # Método para verificação.
    def _verificar_id(self, valor):
        """Método para verificação de id"""
        self.__verificar_id_tipo_invalido(valor)
        self.__verificar_id_vazio(valor)

        self.id = valor
        return self.id
    
    # Método auxiliar. 
    def __verificar_id_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para numero"""
        if not isinstance(valor, int):
            raise TypeError("O ID deve ser um número.")
        
    # Método auxiliar.
    def __verificar_id_vazio(self, valor):
        """Método auxiliar para verificação de número negativo"""
        if valor < 0:
            raise ValueError("O ID não pode ser negativo.")
        
     # Método para verificação.
    def _verificar_nome(self, valor):
        """Método para verificação de nome"""
        self.__verificar_nome_tipo_invalido(valor)
        self.__verificar_nome_vazio(valor)

        self.nome = valor
        return self.nome
    
    # Método auxiliar.
    def __verificar_nome_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para nome"""
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
        
     # Método auxiliar.
    def __verificar_nome_vazio(self, valor):
        """Método auxiliar para verificar nomes vazios"""
        if not valor.strip():
            raise ValueError("O nome não pode estar vazio.")

    # Similar ao ToString.
    def __str__(self) -> str:
        return (
            f"super().__str__()"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição estadual: {self.inscricao_estadual}"
            )