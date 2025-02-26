def get_mask_card_number(card_number: str) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
     Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.
    То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками,
     номер разбит по блокам по 4 цифры, разделенным пробелами."""

    masked_card_number = ""

    for i, x in enumerate(card_number):
        if i % 4 == 0:
            masked_card_number += " "
        if i <= 5 or i >= (len(card_number) - 4):
            masked_card_number += x
        else:
            masked_card_number += "*"
    masked_card_number = masked_card_number.strip(" ")
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
     где X — это цифра номера. То есть видны только последние 4 цифры номера,
      а перед ними — две звездочки."""
    account_number = "****" + account_number
    account_number = account_number[-4:]
    account_number = account_number.replace("*", "")
    return f"**{account_number}"
