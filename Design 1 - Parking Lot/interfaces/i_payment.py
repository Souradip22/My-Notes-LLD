from abc import ABC, abstractmethod

class Payment(ABC):
  
  def __init__(self, amount, status, timestamp):
    self.amount = amount
    self.status = status # Refers to the PaymentStatus enum
    self.timestamp = timestamp

  @abstractmethod
  def initiate_transaction(self):
    pass