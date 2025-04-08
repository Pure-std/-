from typing import Any

from src import generators, processing, read, utils


def ask_user_input(available_options: tuple, false_option_reply: str = "", info: str = "") -> Any:
    """
    Шаблон для запроса информации от пользователя.
    """
    while True:
        if info != "":
            print(info)
        user_input = input().upper()
        if user_input in available_options:
            return user_input
        else:
            if false_option_reply != "":
                print(false_option_reply)


def main() -> None:
    """
    Функция приложения. Отвечает за основную логику проекта с пользователем и связывает функциональности между собой.
    """
    filepaths = ("data/operations.json", "data/transactions.csv", "data/transactions_excel.xlsx")
    file_format = ""
    status = ""
    do_sort_by_date = ""
    do_sort_by_ascension = ""
    only_rub_transactions = ""
    filter_by_word = ""

    file_format = ask_user_input(
        ("1", "2", "3"),
        "Введите цифру которая соответствует одной из опций",
        """
    Привет! Добро пожаловать в программу работы
    с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """,
    )

    print(f"Для обработки выбран {["JSON", "CSV", "XLSX"][int(file_format) - 1]}-файл.")

    status = ask_user_input(
        ("EXECUTED", "CANCELED", "PENDING"),
        "Данный статус операции недоступен. Выберите доступный статус.",
        """
    Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    """,
    )

    print(f'Операции отфильтрованы по статусу "{status}"')

    do_sort_by_date = ask_user_input(("ДА", "НЕТ"), "Впишите Да/Нет", "Отсортировать операции по дате? Да/Нет")
    if do_sort_by_date == "ДА":
        do_sort_by_ascension = ask_user_input(("ДА", "НЕТ"), "Впишите Да/Нет", "Отсортировать по возрастанию? Да/Нет")
    only_rub_transactions = ask_user_input(
        ("ДА", "НЕТ"), "Впишите Да/Нет", "Выводить только рублевые транзакции? Да/Нет"
    )
    filter_by_word = ask_user_input(
        ("ДА", "НЕТ"), "Впишите Да/Нет", "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
    )

    print("Распечатываю итоговый список транзакций...")

    if file_format == "1":
        filedata = utils.read_json_data(filepaths[0])
    elif file_format == "2":
        filedata = read.read_csv(filepaths[1])
    else:
        filedata = read.xlsx_read(filepaths[2])
    if len(filedata) == 0:
        print("Файл пустой.")
        return None
    filedata = processing.filter_by_state(filedata, status)
    if do_sort_by_date == "ДА":
        filedata = processing.sort_by_date(filedata, do_sort_by_ascension == "НЕТ")
    if len(filedata) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия")
        return None
    if only_rub_transactions == "ДА":
        filedata = filedata[1:]
        filedata = [x for x in generators.filters_by_currency(filedata, "RUB", (file_format == "1"))]
    if len(filedata) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия")
        return None
    if filter_by_word == "ДА":
        print("Введите слово-фильтр.")
        filedata = processing.filter_by_description(filedata, input())
    if len(filedata) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия")
        return None
    else:
        print(f"Всего банковских операций в выборке: {len(filedata)}")
        for transaction in filedata:
            print(transaction)
        return None


main()
