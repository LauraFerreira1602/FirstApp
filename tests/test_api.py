import pytest

from mock import patch

# from pasta.arquivo import função
from API.Exemplo import exemplo_cep

@patch('API.Exemplo.requests.get')
def test_exemplo_cep(mock_get):
    # Arrange
    mock_get.return_value.json.return_value = {
        "logradouro": "Rua de kakutaro",
    }
    cep = "123456"

    # Act
    resultado = exemplo_cep("123456")

    # Assert
    assert resultado ["logradouro"] == "Rua de kakutaro"
    mock_get.assert_called_with(f"https://viacep.com.br/ws/{cep}/json/")