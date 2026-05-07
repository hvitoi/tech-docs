from __future__ import annotations

import threading
from decimal import Decimal
from uuid import UUID, uuid4


class Account:
    def __init__(self):
        self.account_id: UUID = uuid4()
        self.balance: Decimal = Decimal(0)
        # Reentrant lock is necessary because on transfer the lock is acquired twice (for each account): first on the "with" statement and second on the withdraw or deposit operations
        self._lock = threading.RLock()

    def deposit(self, amount: Decimal) -> None:
        with self._lock:
            self.balance += amount

    def withdraw(self, amount: Decimal) -> bool:
        with self._lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False

    def transfer_money(
        self,
        to_account: Account,
        amount: Decimal,
    ):
        first, second = sorted((self, to_account), key=lambda a: a.account_id)

        # The order of acquiring the locks is to prevent deadlocks
        # Thread 1: transfer_money(A, B, 50)   # wants A._lock then B._lock
        # Thread 2: transfer_money(B, A, 30)   # wants B._lock then A._lock
        # T1 acquires A._lock  ──┐
        # T2 acquires B._lock    │  ── now both wait forever
        # T1 wants  B._lock  ◄───┤
        # T2 wants  A._lock  ◄───┘
        with first._lock, second._lock:
            if self.withdraw(amount):
                to_account.deposit(amount)
                return True
            return False
