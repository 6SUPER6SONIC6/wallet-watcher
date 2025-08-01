import argparse
from time import sleep

from pyfiglet import Figlet
from rich.console import Console

from history import add_address_to_history, get_history_table
from utils import is_valid_ethereum_address
from wallet_checker import get_wallet_data, get_wallet_table


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-w", "--wallet", help="The Ethereum wallet address to check.")
    args_parser.add_argument("-H", "--history", action="store_true", help="Show your lookup history")
    args = args_parser.parse_args()

    console = Console()

    if args.history:
        print(get_header("History"))
        history = get_history_table()
        if not history:
            console.print("[red]Your history is empty.[/]")
            return
        console.print(history)
    elif args.wallet:
        if not is_valid_ethereum_address(args.wallet):
            print(get_header("Error"))
            console.print("[red]Invalid Ethereum address. Please enter valid Ethereum address.[/]")
            return
        with console.status("[bold magenta]Fetching wallet data...", spinner="aesthetic", spinner_style="bold magenta"):
            print(get_header("Wallet Watcher"))
            wallet_data = get_wallet_data(args.wallet)

            if not wallet_data:
                console.print("[red]Error fetching wallet data. Please try again.[/]")
                return

            add_address_to_history(wallet_data["address"])
            sleep(0.7)

        console.print(get_wallet_table(wallet_data))
    else:
        args_parser.print_help()


def get_header(text: str = "Wallet Watcher") -> str:
    figlet = Figlet(font="slant", width=200)
    return figlet.renderText(text)


if __name__ == "__main__":
    main()
