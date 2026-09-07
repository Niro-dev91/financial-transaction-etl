import csv
from datetime import datetime
from decimal import Decimal

from models.transaction import Transaction


def read_transactions(file_path: str) -> list[Transaction]:

    transactions = []

    with open(
        file_path,
        mode="r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            transaction = Transaction(
                transaction_id=row["transaction_id"].strip(),
                customer_id=row["customer_id"].strip(),
                transaction_type=row["type"].strip().upper(),
                amount=Decimal(row["amount"]),
                currency=row["currency"].strip().upper(),
                status=row["status"].strip().upper(),
                transaction_date=datetime.strptime(
                    row["date"],
                    "%Y-%m-%d"
                ).date()
            )

            transactions.append(transaction)

    return transactions