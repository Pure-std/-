def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """
    Принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    filtered_list = []
    for x in operations:
        if x["state"] == state:
            filtered_list.append(x)
    return filtered_list


def sort_by_date(operations: list, reverse_parameter: bool = True) -> list:
    """
    Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате
    (date).
    """
    return sorted(operations, key=lambda d: d["date"], reverse=reverse_parameter)
