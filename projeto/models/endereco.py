from projeto.models.enums.unidadefederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self._logradouro = logradouro
        self._numero = numero
        self._complemento = complemento
        self._cep = cep
        self._cidade = cidade
        self._uf = uf