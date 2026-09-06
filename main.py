import csv


with open(
    "data/transactions.csv",
    mode="r",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        transaction_id = row["transaction_id"]
        amount = float(row["amount"])

        if amount <= 0:
            print(
                f"INVALID: {transaction_id} "
                f"amount={amount}"
            )
        else:
            print(
                f"VALID: {transaction_id} "
                f"amount={amount}"
            )