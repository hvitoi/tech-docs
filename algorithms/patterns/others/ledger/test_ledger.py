import unittest
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal
from time import time

from ledger import Account, InsufficientFunds, Ledger


class TestLedger(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger()
        self.alice = Account()
        self.bob = Account()
        self.ledger.deposit(self.alice, Decimal(1000))
        self.ledger.deposit(self.bob, Decimal(500))

    def test_deposit_increases_balance(self):
        self.ledger.deposit(self.alice, Decimal(50))
        self.assertEqual(self.alice.balance, Decimal(1050))

    def test_withdraw_decreases_balance(self):
        self.ledger.withdraw(self.alice, Decimal(200))
        self.assertEqual(self.alice.balance, Decimal(800))

    def test_transfer_moves_money(self):
        self.ledger.transfer(self.alice, self.bob, Decimal(200))
        self.assertEqual(self.alice.balance, Decimal(800))
        self.assertEqual(self.bob.balance, Decimal(700))

    def test_insufficient_funds_raises_and_preserves_balance(self):
        with self.assertRaises(InsufficientFunds):
            self.ledger.withdraw(self.alice, Decimal(99999))
        self.assertEqual(self.alice.balance, Decimal(1000))  # unchanged

    def test_invalid_amount_raises(self):
        for bad in (Decimal(0), Decimal(-1)):
            with self.assertRaises(ValueError):
                self.ledger.deposit(self.alice, bad)

    def test_vault_liability_equals_negative_customer_total(self):
        # Core accounting identity: vault is always exactly the negative of the
        # total customer balance. If this ever breaks, money was created or destroyed.
        self.assertEqual(
            self.ledger.vault.balance,
            -(self.alice.balance + self.bob.balance),
        )

    def test_replay_matches_cached_balance(self):
        for account in (self.alice, self.bob, self.ledger.vault):
            self.assertEqual(self.ledger.replay_balance(account), account.balance)

    def test_concurrent_transfers_preserve_total_no_deadlock(self):
        # Bidirectional transfers under contention — surfaces deadlocks, torn
        # writes between the log and the balances, and cache/log drift.
        initial_total = self.alice.balance + self.bob.balance

        def hammer():
            for _ in range(50):
                try:
                    self.ledger.transfer(self.alice, self.bob, Decimal(7))
                except InsufficientFunds:
                    pass
                try:
                    self.ledger.transfer(self.bob, self.alice, Decimal(11))
                except InsufficientFunds:
                    pass

        start = time()
        with ThreadPoolExecutor(max_workers=20) as pool:
            for _ in range(20):
                pool.submit(hammer)
            # Exiting the `with` calls shutdown(wait=True) — joins every submitted task.
        elapsed = time() - start

        self.assertEqual(self.alice.balance + self.bob.balance, initial_total)
        self.assertEqual(self.ledger.replay_balance(self.alice), self.alice.balance)
        self.assertEqual(self.ledger.replay_balance(self.bob), self.bob.balance)
        self.assertEqual(self.ledger.vault.balance, -(self.alice.balance + self.bob.balance))
        self.assertLess(elapsed, 5)


if __name__ == "__main__":
    unittest.main()
