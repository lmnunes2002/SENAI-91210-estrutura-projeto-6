from enum import Enum

class UnidadeFederativa(Enum):
    # Atribuindo valores ao Enum.
    BAHIA = "Bahia", "BA"
    SAO_PAULO = "São Paulo", "SP"
    RIO_DE_JANEIRO = "Rio de Janeiro", "RJ"
    
    # Construtor.
    def __init__(self, nome, sigla) -> None:
        self.nome = nome
        self.sigla = sigla