import os

import requests
from dotenv import load_dotenv


def transaction_amount_rub(transaction: dict) -> float | None:
    """
    функция, которая принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли
    """
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency != "RUB":
        load_dotenv()
        exchange_api_token = os.getenv("EXCHANGE_RATES_DATA_API_KEY")
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
            f"{currency}&amount={transaction["operationAmount"]["amount"]}"
        )
        headers = {"apikey": exchange_api_token}
        try:
            response = requests.request("GET", url, headers=headers)
            status_code = response.status_code
            try:
                return float(response.json()["result"])
            except Exception as e:
                print(f"Error at external_api.py: {e}\nstatus code: {status_code}")
                return None
        except Exception as e:
            print(f"Error at external_api.py: {e}")
            return None
    else:
        return float(transaction["operationAmount"]["amount"])
