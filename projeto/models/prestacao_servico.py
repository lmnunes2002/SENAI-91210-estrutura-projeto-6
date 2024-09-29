from projeto.abstracts.juridica import Juridica
from projeto.models.endereco import Endereco

class PrestacaoServico(Juridica):
    # Construtor
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str, contrato_inicio: str, contrato_fim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.contrato_inicio = self._verificar_contrato_inicio(contrato_inicio)
        self.contrato_fim = self._verificar_contrato_fim(contrato_fim)

    # Método para verificação.
    def _verificar_contrato_inicio(self, valor):
        """Método para verificação de inicio de contrato"""
        self.__verificar_contrato_inicio_tipo_invalido(valor)
        self.__validar_contrato_inicio(valor)

        self.contrato_inicio = valor
        return self.contrato_inicio

    # Método auxiliar.
    def __verificar_contrato_inicio_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para início de contrato"""
        if not isinstance(valor, str):
            raise TypeError("O inicio de contrato deve ser alfa-númerico")

    # Método auxiliar.    
    def __validar_contrato_inicio(self, valor):
        if self.contrato_inicio >= self.contrato_fim:
            raise ValueError("O início do contrato deve ser anterior ao fim do contrato")
        
        self.contrato_inicio = valor
        return valor
    
    # Método para verificação.
    def _verificar_contrato_fim(self, valor):
        """Método para verificação de fim de contrato"""
        self.__verificar_contrato_fim_tipo_invalido(valor)
        self.__validar_contrato_fim(valor)

        self.contrato_fim = valor
        return self.contrato_fim

    # Método auxiliar.
    def __verificar_contrato_fim_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para fim de contrato"""
        if not isinstance(valor, str):
            raise TypeError("O final do contrato deve ser alfa-númerico")

    # Método auxiliar.    
    def __validar_contrato_fim(self, valor):
        if self.contrato_fim <= self.contrato_inicio:
            raise ValueError("O final do contrato deve ser posterior ao inicio do contrato")
        
        self.contrato_fim = valor
        return valor