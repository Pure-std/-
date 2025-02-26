from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """
    Пример для карты
    Visa Platinum 7000792289606361     # входной аргумент
    Visa Platinum 7000 79** **** 6361  # выход функции

    Пример для счета
    Счет 73654108430135874305          # входной аргумент
    Счет **4305                        # выход функции

    """

    card_components = card.split()
    if len(card_components) == 1:
        return card_components[0]
    elif len(card_components) == 0:
        return ""
    card_type = " ".join(card_components[:-1])
    number = card_components[-1]

    if card_type == "Счёт" or card_type == "Счет":
        return f"{card_type} {get_mask_account(number)}"
    else:
        return f"{card_type} {get_mask_card_number(number)}"


def get_date(date: str) -> str:
    """
    Принимает строку в формате "2024-03-11T02:26:18.671407"

    возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").

    """

    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
