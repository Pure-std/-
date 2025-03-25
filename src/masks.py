import logging
from pathlib import Path

filedir  = Path.cwd()
logger = logging.getLogger("masks.py")
# Основная конфигурация logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=filedir.parent / "logs/masks.py.log",  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске


def get_mask_card_number(card_number: str) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
     Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.
    То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками,
     номер разбит по блокам по 4 цифры, разделенным пробелами."""

    logger.info(f'get_mask_card_number: input({card_number})')

    masked_card_number = ""
    try :
        for i, x in enumerate(card_number):
            if i % 4 == 0:
                masked_card_number += " "
            if i <= 5 or i >= (len(card_number) - 4):
                masked_card_number += x
            else:
                masked_card_number += "*"
        masked_card_number = masked_card_number.strip(" ")
        logger.info(f'get_mask_card_number: output({masked_card_number})')
        return masked_card_number
    except Exception as e :
        logger.error(f'get_mask_card_number: error({e})')

def get_mask_account(account_number: str) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
     где X — это цифра номера. То есть видны только последние 4 цифры номера,
      а перед ними — две звездочки."""
    try :
        logger.info(f'get_mask_account: input({account_number})')
        account_number = "****" + account_number
        account_number = account_number[-4:]
        account_number = account_number.replace("*", "")
        logger.info(f'get_mask_account: output({account_number})')
        return f"**{account_number}"
    except Exception as e :
        logger.error(f'get_mask_account: error({e})')