import csv
from datetime import datetime
from pathlib import Path
from typing import Optional

from rich import box
from rich.table import Table

from utils import format_datetime

HISTORY_FILE = Path("data/ww_history.csv")


def add_address_to_history(address: str) -> None:
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    is_history = HISTORY_FILE.exists()
    with open(HISTORY_FILE, "a") as history:
        writer = csv.DictWriter(history, fieldnames=["address", "date"])
        if not is_history:
            writer.writeheader()

        writer.writerow(
            {
                "address": address,
                "date": datetime.today()
            }
        )


def get_history_table() -> Optional[Table]:
    table = Table(
        show_lines=True,
        min_width=80,
        box=box.SQUARE,
    )
    table.add_column("Address")
    table.add_column("Date", justify="right")

    try:
        history = open(HISTORY_FILE, "r")
    except FileNotFoundError:
        return None
    else:
        reader = csv.DictReader(history)
        for row in reader:
            table.add_row(row["address"], format_datetime(row["date"]))
        history.close()

    return table
