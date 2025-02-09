from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """# Пример для карты
    Visa Platinum 7000792289606361  # входной аргумент
    Visa Platinum 7000 79** **** 6361  # выход функции

    # Пример для счета
    Счет 73654108430135874305  # входной аргумент
    Счет **4305  # выход функции"""

    card_type = card[:-16]
    number = card[14:]

    if card_type == "Счёт" or card_type == "Счет":
        return get_mask_account(number)
    else:
        return get_mask_card_number(number)


def get_date(date: str) -> str:
    """Принимает строку в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    return f"{date[:4]}.{date[5:7]}.{date[8:10]}"
