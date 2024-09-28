from projeto.abstracts.juridica import Juridica
from projeto.models.endereco import Endereco

class Fornecedor(Juridica):
    # Construtor
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.produto = self._verificar_produto(produto)

    # Método para verificação.
    def _verificar_id(self, valor):
        """Método auxiliar para verificação de id"""
        self.__verificar_id_tipo_invalido(valor)
        self.__verificar_id_vazio(valor)

        self.id = valor
        return self.id
    
    # Método auxiliar. 
    def __verificar_id_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para numero"""
        if not isinstance(valor, int):
            raise TypeError("O ID deve ser um número")
        
    # Método auxiliar.
    def __verificar_id_vazio(self, valor):
        """Método auxiliar para verificação de número negativo"""
        if valor < 0:
            raise ValueError("O ID não pode ser negativo")
        
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
            raise TypeError("O nome não pode estar vazio.")
    
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
            raise TypeError("O CNPJ não pode estar vazio.")
        
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
            raise TypeError("A inscrição estadual não pode estar vazia.")
    
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
            raise TypeError("O produto não pode estar vazio")

    # Similar ao ToString    
    def apresentar(self):
        return (
            f"Nome: {self.nome}"
        )