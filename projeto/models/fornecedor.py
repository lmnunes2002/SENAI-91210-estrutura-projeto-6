from projeto.abstracts.juridica import Juridica
from projeto.models.endereco import Endereco

class Fornecedor(Juridica):
    # Construtor
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.produto = self._verificar_produto(produto)
    
    # Método para verificação.
    def _verificar_produto(self, valor):
        """Método para verificar produto"""
        self.__verificar_produto_tipo_invalido(valor)
        self.__verificar_produto_vazio(valor)

        self.produto = valor
        return self.produto

    # Método auxiliar.
    def __verificar_produto_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para produto"""
        if not isinstance(valor, str):
            raise TypeError("O produto deve ser um texto")

    # Método auxiliar.    
    def __verificar_produto_vazio(self, valor):
        """Método auxiliar para verificação de produtos vazios"""
        if not valor.strip():
            raise ValueError("O produto não pode estar vazio")

    # Instanciano método abstrato.    
    def apresentar(self):
        return (
            f"Nome: {self.nome}"
        )