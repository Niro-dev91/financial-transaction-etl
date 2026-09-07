from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass
class Transaction:
    transaction_id: str
    customer_id: str
    transaction_type: str
    amount: Decimal
    currency: str
    status: str
    transaction_date: date