import re
from collections import Counter
from typing import Dict, List


def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """
    Принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    filtered_list = []
    for x in operations:
        if x.get("state") == state:
            filtered_list.append(x)
    return filtered_list


def sort_by_date(operations: list, reverse_parameter: bool = True) -> list:
    """
    Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате
    (date).
    """
    return sorted(operations, key=lambda d: d.get("date", ""), reverse=reverse_parameter)


def filter_by_description(operations: list, pattern: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка.
    """
    return [operation for operation in operations if re.search(pattern, operation["description"]) is not None]


def count_operations_by_category(operations: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает операции по категориям с использованием Counter"""
    descriptions = [op.get("description") for op in operations if op.get("description") in categories]
    counts = Counter(descriptions)
    return {category: counts.get(category, 0) for category in categories}
