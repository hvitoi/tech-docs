import unittest
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal

from account import Account, InsufficientFunds


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.alice = Account()
        self.alice.deposit(Decimal(1000))
        self.bob = Account()
        self.bob.deposit(Decimal(500))

    def test_deposit_increases_balance(self):
        self.alice.deposit(Decimal(50))
        self.assertEqual(self.alice.balance, Decimal(1050))

    def test_withdraw_decreases_balance(self):
        self.alice.withdraw(Decimal(400))
        self.assertEqual(self.alice.balance, Decimal(600))

    def test_withdraw_raises_when_insufficient(self):
        with self.assertRaises(InsufficientFunds):
            self.alice.withdraw(Decimal(99999))
        self.assertEqual(self.alice.balance, Decimal(1000))

    def test_transfer_moves_money(self):
        self.alice.transfer_money(self.bob, Decimal(200))
        self.assertEqual(self.alice.balance, Decimal(800))
        self.assertEqual(self.bob.balance, Decimal(700))

    def test_transfer_raises_on_insufficient(self):
        with self.assertRaises(InsufficientFunds):
            self.alice.transfer_money(self.bob, Decimal(99999))
        self.assertEqual(self.alice.balance, Decimal(1000))
        self.assertEqual(self.bob.balance, Decimal(500))

    def test_concurrent_transfers_preserve_total_no_deadlock(self):
        total = self.alice.balance + self.bob.balance

        def hammer():
            for _ in range(50):
                self.alice.transfer_money(self.bob, Decimal(7))
                self.bob.transfer_money(self.alice, Decimal(11))

        with ThreadPoolExecutor(max_workers=20) as executor:
            for _ in range(20):
                executor.submit(hammer)

        self.assertEqual(self.alice.balance + self.bob.balance, total)


if __name__ == "__main__":
    unittest.main()
