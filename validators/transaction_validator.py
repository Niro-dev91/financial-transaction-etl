from models.transaction import Transaction


VALID_TRANSACTION_TYPES = {
    "DEPOSIT",
    "WITHDRAWAL",
    "TRANSFER"
}

VALID_STATUSES = {
    "SUCCESS",
    "FAILED",
    "PENDING"
}

SUPPORTED_CURRENCIES = {
    "LKR",
    "USD"
}


def validate_transaction(
    transaction: Transaction,
    processed_ids: set[str]
) -> list[str]:

    errors = []

    if not transaction.transaction_id:
        errors.append("Transaction ID is required")

    if not transaction.customer_id:
        errors.append("Customer ID is required")

    if transaction.amount <= 0:
        errors.append("Amount must be greater than zero")

    if transaction.transaction_type not in VALID_TRANSACTION_TYPES:
        errors.append("Invalid transaction type")

    if transaction.status not in VALID_STATUSES:
        errors.append("Invalid transaction status")

    if transaction.currency not in SUPPORTED_CURRENCIES:
        errors.append("Unsupported currency")

    if transaction.transaction_id in processed_ids:
        errors.append("Duplicate transaction ID")

    return errors