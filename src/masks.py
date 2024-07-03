def get_mask_card_number(card_number: str) -> str and None:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return None


def get_mask_account(account: str) -> str and None:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if account.isdigit() and len(account) == 20:
        return f"{'*' * 2}{account[16:]}"
    else:
        return None
