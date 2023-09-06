from enum import Enum

class PaymentStatus(Enum):
    COMPLETED = 1
    FAILED = 2
    PENDING = 3
    UNPAID = 4
    REFUNDED = 5