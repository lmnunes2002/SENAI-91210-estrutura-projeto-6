import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.tests.test_endereco import endereco_valido
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def engeheiro_valido():
    engenheiro = Engenheiro(1, "João da Silva", "1234-5678", "joao.silva@example.com", endereco_valido, Sexo.MASCULINO, EstadoCivil.CASADO, "01/01/1980", "123.456.789-00", "12.345.678-9", "123456", Setor.ENGENHARIA, 8000.0, "123456/PR")