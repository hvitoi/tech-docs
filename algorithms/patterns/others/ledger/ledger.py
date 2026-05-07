from dataclasses import dataclass
from decimal import Decimal
from threading import Lock
from uuid import UUID, uuid4


class Account:
    def __init__(self):
        self.account_id: UUID = uuid4()
        self.balance: Decimal = Decimal(0)


@dataclass(frozen=True)
class Entry:
    account_id: UUID
    amount: Decimal


class InsufficientFunds(Exception):
    pass


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
        self._lock = Lock()
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
                raise InsufficientFunds()
            self._journal.append(
                # append the legs (each "side" of the transaction)
                (
                    Entry(from_account.account_id, -amount),
                    Entry(to_account.account_id, +amount),
                )
            )
            from_account.balance -= amount
            to_account.balance += amount

    def balance_of(self, account: Account) -> Decimal:
        """Replay the journal for this account — reconciles against journal"""
        with self._lock:
            return sum(
                (
                    entry.amount
                    for legs in self._journal
                    for entry in legs
                    if entry.account_id == account.account_id
                ),
                Decimal(0),
            )
