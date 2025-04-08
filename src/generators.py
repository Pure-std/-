from typing import Iterator


def filters_by_currency(transactions: list, currency: str, is_json: bool = False) -> Iterator:
    """
    Возвращает итератор, который выдает транзакции, отфильтрованные по заданной валюте.
    """
    if is_json:
        return iter(
            transaction
            for transaction in transactions
            if transaction.get("operationAmount").get("currency").get("code") == currency
        )
    else:
        return iter(transaction for transaction in transactions if transaction.get("currency_code") == currency)


def transaction_descriptions(transactions: list) -> Iterator:
    """
    Генератор, который выдает значение ключа description транзакций.
    """
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(minimal: int, maximal: int) -> Iterator:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX
    в диапазоне от 0000 0000 0000 0000 до 9999 9999 9999 99999.
    """
    num = minimal
    while num <= maximal:
        s = "0" * (16 - (len(str(num)))) + str(num)
        yield f"{s[0:4]} {s[4:8]} {s[8:12]} {s[12:]}"
        num += 1
