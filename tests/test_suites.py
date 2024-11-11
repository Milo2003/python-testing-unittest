import unittest

from tests_bank_account import BankAccountTests


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_get_balance_returns_current_balance"))
    suite.addTest(BankAccountTests("test_deposit_increases_balance_by_deposit_amount"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
