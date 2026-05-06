import threading
import uuid


class Account:
    def __init__(self):
        self.account_id = uuid.uuid4()
        self.balance = 0
        self._lock = threading.RLock()

    def deposit(self, amount):
        with self._lock:
            self.balance += amount

    def withdraw(self, amount):
        with self._lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False

    def get_balance(self):
        with self._lock:
            return self.balance


class Ledger:
    @staticmethod
    def transfer_money(from_account, to_account, amount):
        if from_account.account_id < to_account.account_id:
            first, second = from_account, to_account
        else:
            first, second = to_account, from_account

        with first._lock, second._lock:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                return True
            return False
