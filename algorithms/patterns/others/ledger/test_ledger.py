import threading
import unittest
from time import time

from ledger import Account, Ledger


class TestLedger(unittest.TestCase):
    def test_concurrent_transfers_preserve_total(self):
        num_threads = 5
        transfer_amount = 50

        acc1 = Account()
        acc1.deposit(1000)
        acc2 = Account()
        acc2.deposit(1000)
        initial_total = acc1.get_balance() + acc2.get_balance()

        def transfer() -> None:
            Ledger.transfer_money(acc1, acc2, transfer_amount)

        threads = [threading.Thread(target=transfer) for _ in range(num_threads)]
        start = time()
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        elapsed = time() - start

        final_total = acc1.get_balance() + acc2.get_balance()
        self.assertEqual(final_total, initial_total, "total balance must be conserved")
        self.assertLess(elapsed, 5, "potential deadlock detected")


if __name__ == "__main__":
    unittest.main()
