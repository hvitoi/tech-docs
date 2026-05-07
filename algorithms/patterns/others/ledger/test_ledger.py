import threading
import unittest
from decimal import Decimal
from time import time

from ledger import Account, InsufficientFunds, Ledger


class TestLedger(unittest.TestCase):
    def test_deposit_withdraw_transfer(self):
        ledger = Ledger()
        alice, bob = Account(), Account()

        ledger.deposit(alice, Decimal(1000))
        ledger.deposit(bob, Decimal(500))
        ledger.transfer(alice, bob, Decimal(200))
        ledger.withdraw(bob, Decimal(50))

        self.assertEqual(alice.balance, Decimal(800))
        self.assertEqual(bob.balance, Decimal(650))

    def test_insufficient_funds_raises(self):
        ledger = Ledger()
        alice = Account()
        ledger.deposit(alice, Decimal(100))

        with self.assertRaises(InsufficientFunds):
            ledger.withdraw(alice, Decimal(101))
        # Balance unchanged after the failed call.
        self.assertEqual(alice.balance, Decimal(100))

    def test_invalid_amount_raises(self):
        ledger = Ledger()
        alice = Account()
        for bad in (Decimal(0), Decimal(-1)):
            with self.assertRaises(ValueError):
                ledger.deposit(alice, bad)

    def test_vault_liability_equals_negative_customer_total(self):
        # The accounting identity: the ledger's vault balance is the negative
        # of the total customer balance at all times.
        ledger = Ledger()
        alice, bob = Account(), Account()
        ledger.deposit(alice, Decimal(1000))
        ledger.deposit(bob, Decimal(700))
        ledger.transfer(alice, bob, Decimal(300))
        ledger.withdraw(alice, Decimal(50))

        self.assertEqual(ledger.vault.balance, -(alice.balance + bob.balance))

    def test_replay_matches_cached_balance(self):
        ledger = Ledger()
        alice, bob = Account(), Account()
        ledger.deposit(alice, Decimal(500))
        ledger.deposit(bob, Decimal(500))
        ledger.transfer(alice, bob, Decimal(100))
        ledger.transfer(bob, alice, Decimal(40))
        ledger.withdraw(alice, Decimal(25))

        for account in (alice, bob, ledger.vault):
            self.assertEqual(ledger.replay_balance(account), account.balance)

    def test_concurrent_transfers_preserve_total(self):
        ledger = Ledger()
        alice, bob = Account(), Account()
        ledger.deposit(alice, Decimal(10000))
        ledger.deposit(bob, Decimal(10000))
        initial_total = alice.balance + bob.balance

        # Bidirectional transfers exercise the locking story end to end —
        # if there were a deadlock or a torn write, this is where it'd show up.
        def hammer():
            for _ in range(50):
                try:
                    ledger.transfer(alice, bob, Decimal(7))
                except InsufficientFunds:
                    pass
                try:
                    ledger.transfer(bob, alice, Decimal(11))
                except InsufficientFunds:
                    pass

        start = time()
        threads = [threading.Thread(target=hammer) for _ in range(20)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        elapsed = time() - start

        self.assertEqual(alice.balance + bob.balance, initial_total, "total must be conserved")
        self.assertEqual(ledger.replay_balance(alice), alice.balance, "replay must match cache")
        self.assertEqual(ledger.replay_balance(bob), bob.balance, "replay must match cache")
        self.assertEqual(ledger.vault.balance, -(alice.balance + bob.balance))
        self.assertLess(elapsed, 5, "potential deadlock detected")


if __name__ == "__main__":
    unittest.main()
