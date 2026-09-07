import csv

from models.transaction import Transaction


def write_valid_transactions(
    file_path: str,
    transactions: list[Transaction]
) -> None:

    with open(
        file_path,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "transaction_id",
            "customer_id",
            "type",
            "amount",
            "currency",
            "status",
            "date"
        ])

        for transaction in transactions:
            writer.writerow([
                transaction.transaction_id,
                transaction.customer_id,
                transaction.transaction_type,
                transaction.amount,
                transaction.currency,
                transaction.status,
                transaction.transaction_date
            ])


def write_rejected_transactions(
    file_path: str,
    rejected_transactions: list[tuple[Transaction, list[str]]]
) -> None:

    with open(
        file_path,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "transaction_id",
            "customer_id",
            "amount",
            "reason"
        ])

        for transaction, errors in rejected_transactions:
            writer.writerow([
                transaction.transaction_id,
                transaction.customer_id,
                transaction.amount,
                "; ".join(errors)
            ])