import csv
from pathlib import Path

import pandas as pd


def read_csv(filepath: str) -> list[dict]:
    filedir = Path.cwd()
    with open(filedir.parent / filepath, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def xlsx_read(filepath: str) -> list[dict]:
    filedir = Path.cwd()
    reader = pd.read_excel(filedir.parent / filepath)
    return reader.to_dict("records")
