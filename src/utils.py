import json
import logging
from pathlib import Path
from typing import Any

filedir = Path.cwd()
logger = logging.getLogger("utils.py")
# Основная конфигурация logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=filedir.parent / "logs/utils.py.log",  # Запись логов в файл
    filemode="a",
)  # Перезапись файла при каждом запуске


def read_json_data(filepath: str) -> Any:
    """
    функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    :param filepath:
    :return:
    """
    logger.info(f"read_json_data: input({filepath})")
    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            data = json.load(file)
    except Exception as e:
        logger.error(f"read_json_data: {e}")
        data = []
    logger.info(f"read_json_data: output({data})")
    return data
