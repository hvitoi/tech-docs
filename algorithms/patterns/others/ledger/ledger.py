import threading
from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Entry:
    """One leg of a transaction. Positive credits the account, negative debits it."""

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
    An append-only log of double-entry transactions.

    Each transfer is a pair of entries summing to zero. The log is the source of
    truth — account balances are a cache that can be rebuilt by replaying the log.

      - immutable: entries are never edited; corrections are new entries
      - atomic: both legs of a transfer commit or neither does
      - ordered: log index is the canonical sequence
      - reconcilable: replay reproduces every balance

    Concurrency: one ledger-wide lock serializes every post and every read, so
    log appends and balance updates always commit together. Per-account locks
    would let disjoint transfers run in parallel, but require canonical lock-order
    acquisition (e.g. sorted by account_id) to avoid deadlocking with an
    opposite-direction transfer:
        T1: transfer(A, B, 50)   wants A then B
        T2: transfer(B, A, 30)   wants B then A   <- deadlock without ordering
    Under Python's GIL the throughput point is moot, so prefer simple.
    """

    def __init__(self):
        self._log: list[tuple[Entry, Entry]] = []
        self._lock = threading.Lock()
        # Bookkeeping counterparty for deposits and withdrawals. Its balance goes
        # negative — that negative is the ledger's net liability to customers.
        # A well-formed ledger satisfies vault.balance == -sum(customer balances).
        self.vault = Account()

    def deposit(self, account: Account, amount: Decimal) -> None:
        self.transfer(self.vault, account, amount)

    def withdraw(self, account: Account, amount: Decimal) -> None:
        self.transfer(account, self.vault, amount)

    def transfer(self, src: Account, dst: Account, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        with self._lock:
            # The vault is the bookkeeping counterparty, allowed to go negative.
            # Customer accounts must stay solvent.
            if src is not self.vault and src.balance < amount:
                raise InsufficientFunds(
                    f"{src.account_id} has {src.balance}, needs {amount}"
                )
            entries = (
                Entry(src.account_id, -amount),
                Entry(dst.account_id, +amount),
            )
            assert sum((e.amount for e in entries), Decimal(0)) == 0  # double-entry invariant
            self._log.append(entries)
            src.balance -= amount
            dst.balance += amount

    def replay_balance(self, account: Account) -> Decimal:
        """Sum every entry against this account — reconciles against the cached balance."""
        with self._lock:
            return sum(
                (
                    e.amount
                    for legs in self._log
                    for e in legs
                    if e.account_id == account.account_id
                ),
                Decimal(0),
            )
