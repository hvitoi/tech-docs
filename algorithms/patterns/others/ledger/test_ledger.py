import unittest
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal

from ledger import Account, InsufficientFunds, Ledger


class TestLedger(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger()
        self.alice = Account()
        self.ledger.deposit(self.alice, Decimal(1000))
        self.bob = Account()
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

    def test_insufficient_funds_raises(self):
        with self.assertRaises(InsufficientFunds):
            self.ledger.withdraw(self.alice, Decimal(99999))
        self.assertEqual(self.alice.balance, Decimal(1000))

    def test_replay_matches_cached_balance(self):
        self.ledger.transfer(self.alice, self.bob, Decimal(100))
        self.ledger.withdraw(self.alice, Decimal(25))
        self.assertEqual(self.ledger.balance_of(self.alice), self.alice.balance)
        self.assertEqual(self.ledger.balance_of(self.bob), self.bob.balance)

    def test_concurrent_transfers_preserve_total(self):
        total = self.alice.balance + self.bob.balance

        def hammer():
            for _ in range(50):
                self.ledger.transfer(self.alice, self.bob, Decimal(7))
                self.ledger.transfer(self.bob, self.alice, Decimal(11))

        with ThreadPoolExecutor(max_workers=20) as executor:
            for _ in range(20):
                executor.submit(hammer)

        self.assertEqual(self.alice.balance + self.bob.balance, total)


if __name__ == "__main__":
    unittest.main()
