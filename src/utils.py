import json
from typing import Any


def read_json_data(filepath: str) -> Any:
    """
    функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    :param filepath:
    :return:
    """
    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Exception at utils.py: {e}")
        data = []
    return data
