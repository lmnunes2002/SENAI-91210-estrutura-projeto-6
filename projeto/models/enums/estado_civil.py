from enum import Enum

class EstadoCivil(Enum):
    # Atribuindo valores ao Enum.
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"

    # Construtor
    def __init__(self, texto) -> None:
        self.texto = texto