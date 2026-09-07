from services.transaction_reader import read_transactions
from services.transaction_writer import (
    write_valid_transactions,
    write_rejected_transactions
)
from validators.transaction_validator import validate_transaction


INPUT_FILE = "data/transactions.csv"
VALID_OUTPUT_FILE = "output/clean_transactions.csv"
REJECTED_OUTPUT_FILE = "output/rejected_transactions.csv"


def main():

    print("Financial Transaction ETL started")

    transactions = read_transactions(INPUT_FILE)

    valid_transactions = []
    rejected_transactions = []

    processed_ids = set()

    for transaction in transactions:

        errors = validate_transaction(
            transaction,
            processed_ids
        )

        if errors:
            rejected_transactions.append(
                (transaction, errors)
            )
        else:
            valid_transactions.append(transaction)

        processed_ids.add(
            transaction.transaction_id
        )

    write_valid_transactions(
        VALID_OUTPUT_FILE,
        valid_transactions
    )

    write_rejected_transactions(
        REJECTED_OUTPUT_FILE,
        rejected_transactions
    )

    print(
        f"Total transactions: {len(transactions)}"
    )

    print(
        f"Valid transactions: {len(valid_transactions)}"
    )

    print(
        f"Rejected transactions: {len(rejected_transactions)}"
    )

    print("Financial Transaction ETL completed")


if __name__ == "__main__":
    main()