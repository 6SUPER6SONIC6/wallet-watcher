import re
from datetime import datetime


def is_valid_ethereum_address(address: str) -> bool:
    return bool(re.match(r"^0x[A-Fa-f0-9]{40}$", address))

def format_amount(amount: float) -> str:
    if amount == 0:
        return "0"
    elif amount < 0.01:
        return f"{amount:.6f}".rstrip("0").rstrip(".")
    elif amount < 1:
        return f"{amount:.4f}".rstrip("0").rstrip(".")
    else:
        return f"{amount:.2f}".rstrip("0").rstrip(".")


def is_spam_token(token_info) -> bool:
    spam_keywords = ["http", ".com", "claim", "gift", "visit", "earn", "free"]
    token_name = token_info.get("name", None)
    token_symbol = token_info.get("symbol", None)
    if not token_info["price"]:
        return True
    if token_info["totalSupply"] == "0":
        return True
    for keyword in spam_keywords:
        if keyword in token_name:
            return True
        if keyword in token_symbol:
            return True
    return False


def format_datetime(dt_str: str) -> str:
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f")
    return dt.strftime("%d %b %Y, %H:%M")
