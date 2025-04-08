import csv

import pandas as pd


def read_csv(filepath: str) -> list[dict]:
    """Функция для чтения csv файлов. Принимает путь до файла"""
    with open(filepath, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def xlsx_read(filepath: str) -> list[dict]:
    """Функция для чтения xlsx файлов. Принимает путь до файла"""
    reader = pd.read_excel(filepath)
    return reader.to_dict("records")
