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
        self._lock = threading.RLock()


class Ledger:
    """
    An append-only log of double-entry transactions.

    Each transfer is a pair of entries summing to zero. The log is the source of
    truth — account balances are a cache that can be rebuilt by replaying the log.

      - immutable: entries are never edited; corrections are new entries
      - atomic: both legs of a transfer commit or neither does
      - ordered: log index is the canonical sequence
      - reconcilable: replay reproduces every balance
    """

    def __init__(self):
        self._log: list[tuple[Entry, Entry]] = []
        self._log_lock = threading.Lock()
        # External-world counterparty. Every deposit is a transfer from here; every
        # withdrawal is a transfer to here. Its balance goes negative — that negative
        # is the ledger's net liability to customers. A well-formed ledger satisfies
        #   self.vault.balance == -sum(customer balances)
        self.vault = Account()

    def deposit(self, account: Account, amount: Decimal) -> None:
        self.transfer(self.vault, account, amount)

    def withdraw(self, account: Account, amount: Decimal) -> None:
        self.transfer(account, self.vault, amount)

    def transfer(self, src: Account, dst: Account, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")

        # Acquire account locks in a canonical order so two threads transferring in
        # opposite directions can't deadlock:
        #   T1: transfer(A, B, 50)   wants A then B
        #   T2: transfer(B, A, 30)   wants B then A   <- deadlock without ordering
        first, second = sorted((src, dst), key=lambda a: a.account_id)
        with first._lock, second._lock:
            # The vault is the bookkeeping counterparty, not an asset — it's allowed
            # to go negative. Customer accounts must stay solvent.
            if src is not self.vault and src.balance < amount:
                raise InsufficientFunds(f"{src.account_id} has {src.balance}, needs {amount}")
            entries = (
                Entry(src.account_id, -amount),
                Entry(dst.account_id, +amount),
            )
            assert sum((e.amount for e in entries), Decimal(0)) == 0  # double-entry invariant
            with self._log_lock:
                self._log.append(entries)
            src.balance -= amount
            dst.balance += amount

    def replay_balance(self, account: Account) -> Decimal:
        """Sum every entry against this account — reconciles against the cached balance."""
        return sum(
            (e.amount for legs in self._log for e in legs if e.account_id == account.account_id),
            Decimal(0),
        )
