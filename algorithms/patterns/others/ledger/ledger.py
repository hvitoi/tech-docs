import threading
from uuid import UUID, uuid4


class Account:
    def __init__(self):
        self.account_id: UUID = uuid4()
        self.balance: int = 0
        self._lock = threading.RLock()

    def deposit(self, amount: int) -> None:
        with self._lock:
            self.balance += amount

    def withdraw(self, amount: int) -> bool:
        with self._lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False


class Ledger:
    """
    A ledger is an append-only log of transactions
    Every transaction is double-entry: a transfer of $50 from A to B is two paired entries (-50 on A, +50 on B) that must sum to zero.
    Immutable (never edit, only append corrections), atomic (both legs of a transfer commit or neither), ordered (sequence matters), reconcilable (you can replay the log and verify balances).
    """

    @staticmethod
    def transfer_money(
        from_account: Account,
        to_account: Account,
        amount: int,
    ):
        first, second = sorted((from_account, to_account), key=lambda a: a.account_id)

        # The order of acquiring the locks is to prevent deadlocks
        # Thread 1: transfer_money(A, B, 50)   # wants A._lock then B._lock
        # Thread 2: transfer_money(B, A, 30)   # wants B._lock then A._lock
        # T1 acquires A._lock  ──┐
        # T2 acquires B._lock    │  ── now both wait forever
        # T1 wants  B._lock  ◄───┤
        # T2 wants  A._lock  ◄───┘
        with first._lock, second._lock:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                return True
            return False
