from enum import Enum

class Setor(Enum):
    # Atribuindo valores ao Enum.
    ENGENHARIA = "Engenharia"
    SAUDE = "Saúde"
    JURIDICO = "Jurídico"

    # Construtor.
    def __init__(self, texto: str) -> None:
        self.texto = texto