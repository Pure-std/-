## Описание:
Этот репозиторий содержит решение домашней работы.
## Тестирование
Весь код на 100% покрыт тестами два раза(параметризацией и фикстурами). Все тесты хранятся в отдельной папке tests.
Тесты написанны с использованием pytest. Включены нестандартные и пограничные случаи.
## generators.py
### `filters_by_currency(transactions: list, currency: str)`
Фильтрует транзакции по заданной валюте.

**Параметры:**
- `transactions` - список транзакций
- `currency` - трехбуквенный код валюты (например, "USD")

**Возвращает:**
- Итератор по отфильтрованным транзакциям

**Пример:**
```python
transactions = [
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    },
    {
        "operationAmount": {
            "currency": {"code": "EUR"}
        }
    }
]

for tx in filters_by_currency(transactions, "USD"):
    print(tx)  # Выведет первую транзакцию
```
### `transaction_descriptions(transactions: list)`
Генерирует описания транзакций.

Параметры:

transactions - список транзакций

Возвращает:

Итератор по описаниям (может содержать None)

**Пример:**
```python
transactions = [
    {"description": "Payment"},
    {"description": "Transfer"},
    {}  # Транзакция без описания
]

list(transaction_descriptions(transactions))
# ['Payment', 'Transfer', None]
```
card_number_generator(minimal: int, maximal: int) -> Iterator
Генерирует номера карт в заданном диапазоне.

Параметры:

minimal - начальный номер (включительно)

maximal - конечный номер (включительно)

Возвращает:

Итератор по номерам в формате "XXXX XXXX XXXX XXXX"

**Пример:**
```
python
Copy
list(card_number_generator(1, 3))
# [
#   '0000 0000 0000 0001',
#   '0000 0000 0000 0002',
#   '0000 0000 0000 0003'
# ]

list(card_number_generator(123456, 123456))
# ['0000 0000 0012 3456']
```
## decorators.py
Модуль для реализации декораторов.

**log**
```
Декоратор для логирования вызовов функций.

Может записывать логи как в консоль, так и в файл.
```
## Установка:

1. Клонируйте репозиторий:

git clone https://github.com/Pure-std/-.git
## Документация:

Для получения дополнительной информации обратитесь к несуществующей документации.

## Лицензия:

Этот проект лицензирован по... он не лицензирован!
