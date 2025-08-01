import requests
from rich import box
from rich.table import Table
from rich.text import Text

from utils import format_amount, is_spam_token


API_KEY = "freekey"
BASE_URL = "https://api.ethplorer.io/"

def get_wallet_data(address: str):
    try:
        wallet_result = requests.get(
            f"{BASE_URL}getAddressInfo/{address}?apiKey={API_KEY}")
    except requests.RequestException:
        return None
    else:
        if wallet_result.status_code != 200:
            return None

        json_data = wallet_result.json()
        return {
            "address": json_data["address"],
            "tokens": parse_wallet(json_data)
        }


def parse_wallet(json_data) -> list:
    tokens = []
    eth = json_data["ETH"]
    eth_balance = eth["balance"]
    eth_rate = eth["price"]["rate"]
    eth_usd_value = eth_balance * eth_rate

    tokens.append(
        {
            "name": "Ethereum",
            "symbol": "ETH",
            "balance": format_amount(eth_balance),
            "usd_value": format_amount(eth_usd_value)
        }
    )

    if json_data.get("tokens"):

        for token in json_data["tokens"]:
            token_info = token["tokenInfo"]
            if not is_spam_token(token_info):
                raw_balance = int(token["rawBalance"])
                decimals = int(token_info["decimals"])
                balance = raw_balance / (10 ** decimals)
                price = token_info["price"]
                rate = float(price["rate"])
                usd_value = balance * rate

                tokens.append(
                    {
                        "name": token_info["name"],
                        "symbol": token_info["symbol"],
                        "balance": format_amount(balance),
                        "usd_value": format_amount(usd_value)
                    }
                )

    return tokens


def get_wallet_table(wallet_data):
    table = Table(
        title=wallet_data["address"],
        show_lines=True,
        show_header=True,
        min_width=80,
        box=box.SQUARE,
    )

    table.add_column("Token", justify="left")
    table.add_column("Amount", justify="right")
    table.add_column("Value", justify="right")

    for token in wallet_data["tokens"]:
        name = Text(token["name"], style="magenta")
        symbol = Text(f"({token['symbol']})", style="bright_black")
        table.add_row(name + symbol, token["balance"], f"${token['usd_value']}")

    return table
