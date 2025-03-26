from unittest.mock import Mock, patch

import requests

from src.external_api import transaction_amount_rub


@patch("requests.request")
@patch.dict("os.environ", {"EXCHANGE_RATES_DATA_API_KEY": "test_api_key"})
def test_transaction_amount_rub_rub(mock_request: Mock) -> None:
    transaction = {"operationAmount": {"currency": {"code": "RUB"}, "amount": "100.0"}}
    result = transaction_amount_rub(transaction)
    assert result == 100.0
    mock_request.assert_not_called()


@patch("requests.request")
@patch.dict("os.environ", {"EXCHANGE_RATES_DATA_API_KEY": "test_api_key"})
def test_transaction_amount_rub_foreign_currency(mock_request: Mock) -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.5}
    mock_request.return_value = mock_response

    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": "100.0"}}

    result = transaction_amount_rub(transaction)
    assert result == 7500.5
    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.0",
        headers={"apikey": "test_api_key"},
    )


@patch("requests.request")
@patch.dict("os.environ", {"EXCHANGE_RATES_DATA_API_KEY": "test_api_key"})
def test_transaction_amount_rub_api_error(mock_request: Mock) -> None:
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"error": "Internal Server Error"}
    mock_request.return_value = mock_response

    transaction = {"operationAmount": {"currency": {"code": "EUR"}, "amount": "200.0"}}

    result = transaction_amount_rub(transaction)
    assert result is None


@patch("requests.request")
@patch.dict("os.environ", {"EXCHANGE_RATES_DATA_API_KEY": "test_api_key"})
def test_transaction_amount_rub_request_exception(mock_request: Mock) -> None:
    mock_request.side_effect = requests.exceptions.RequestException("Connection error")

    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": "100.0"}}

    result = transaction_amount_rub(transaction)
    assert result is None
    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.0",
        headers={"apikey": "test_api_key"},
    )


@patch("requests.request")
@patch.dict("os.environ", {"EXCHANGE_RATES_DATA_API_KEY": "test_api_key"})
def test_transaction_amount_rub_missing_result_key(mock_request: Mock) -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": 7500.5}  # Отсутствует 'result'
    mock_request.return_value = mock_response

    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": "100.0"}}

    result = transaction_amount_rub(transaction)
    assert result is None
    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.0",
        headers={"apikey": "test_api_key"},
    )


@patch("requests.request")
@patch("os.getenv")
@patch("src.external_api.load_dotenv")
def test_transaction_amount_rub_missing_api_key(mock_load_dotenv: Mock, mock_getenv: Mock, mock_request: Mock) -> None:
    mock_getenv.return_value = None

    mock_response = Mock()
    mock_response.status_code = 403
    mock_request.return_value = mock_response

    transaction = {"operationAmount": {"currency": {"code": "EUR"}, "amount": "200.0"}}

    result = transaction_amount_rub(transaction)
    assert result is None

    mock_load_dotenv.assert_called_once()

    mock_getenv.assert_called_once_with("EXCHANGE_RATES_DATA_API_KEY")

    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=200.0",
        headers={"apikey": None},
    )
