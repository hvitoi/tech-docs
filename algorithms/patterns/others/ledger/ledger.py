import threading
from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Entry:
    """One leg of a transfer. Positive credits the account, negative debits it."""

    account_id: UUID
    amount: Decimal


class InsufficientFunds(Exception):
    pass


class Account:
    def __init__(self):
        self.account_id: UUID = uuid4()
        self.balance: Decimal = Decimal(0)


class Ledger:
    """
    Append-only journal of double-entry transfers.

    Every balance change is recorded as a pair of entries summing to zero. The
    journal is the source of truth — balances are a cache that can be rebuilt
    by replaying it (see balance_of).

    Deposits and withdrawals are paired with a hidden cash counterparty so the
    journal stays balanced. Cash goes negative — that negative is the ledger's
    net liability to its customers.
    """

    def __init__(self):
        self._journal: list[tuple[Entry, Entry]] = []
        self._lock = threading.Lock()
        self._cash = Account()

    def deposit(self, account: Account, amount: Decimal) -> None:
        self.transfer(self._cash, account, amount)

    def withdraw(self, account: Account, amount: Decimal) -> None:
        self.transfer(account, self._cash, amount)

    def transfer(
        self, from_account: Account, to_account: Account, amount: Decimal
    ) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        with self._lock:
            # Cash is the bookkeeping counterparty, allowed to go negative.
            if from_account is not self._cash and from_account.balance < amount:
                raise InsufficientFunds(
                    f"{from_account.account_id} has {from_account.balance}, needs {amount}"
                )
            self._journal.append(
                (
                    Entry(from_account.account_id, -amount),
                    Entry(to_account.account_id, +amount),
                )
            )
            from_account.balance -= amount
            to_account.balance += amount

    def balance_of(self, account: Account) -> Decimal:
        """Replay the journal for this account — reconciles against the cached balance."""
        with self._lock:
            return sum(
                (
                    e.amount
                    for legs in self._journal
                    for e in legs
                    if e.account_id == account.account_id
                ),
                Decimal(0),
            )
