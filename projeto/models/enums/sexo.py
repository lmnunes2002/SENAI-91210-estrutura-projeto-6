from enum import Enum

class Sexo(Enum):
    # Atribuindo valores ao Enum.
    MASCULINO = "M", "Masculino"
    FEMININO = "F", "Feminino"

    # Construtor.
    def __init__(self, caractere: str, texto: str) -> None:
        self.caractere = caractere
        self.texto = texto