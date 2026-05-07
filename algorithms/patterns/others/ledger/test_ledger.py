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

    def test_replay_matches_cached_balance(self):
        # The journal is the source of truth — replaying it must reproduce
        # whatever the cached balance says.
        self.ledger.transfer(self.alice, self.bob, Decimal(100))
        self.ledger.transfer(self.bob, self.alice, Decimal(40))
        self.ledger.withdraw(self.alice, Decimal(25))
        self.assertEqual(self.ledger.balance_of(self.alice), self.alice.balance)
        self.assertEqual(self.ledger.balance_of(self.bob), self.bob.balance)

    def test_concurrent_transfers_preserve_total_no_deadlock(self):
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
        elapsed = time() - start

        self.assertEqual(self.alice.balance + self.bob.balance, initial_total)
        self.assertEqual(self.ledger.balance_of(self.alice), self.alice.balance)
        self.assertEqual(self.ledger.balance_of(self.bob), self.bob.balance)
        self.assertLess(elapsed, 5)


if __name__ == "__main__":
    unittest.main()
