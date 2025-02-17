def filter_by_state(operations: list, state = "EXECUTED") -> list:
    """"принимает список словарей и опционально значение для ключа state
        (по умолчанию 'EXECUTED').
        Функция возвращает новый список словарей, содержащий только те словари,
        у которых ключ stateсоответствует указанному значению."""
    filtered_list = []
    for x in operations :
        if x["state"] == state :
            filtered_list.append(x)
    return filtered_list
