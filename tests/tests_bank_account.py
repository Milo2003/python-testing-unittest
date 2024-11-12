import unittest
import os
from datetime import datetime
from unittest.mock import patch
from src.exception import InsufficientFundsError
from src.bank_account import BankAccount
from src.exception import WithdrawTimeRestrictionError, WithdrawDayRestrictionError


class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=2000, log_file="transaction_log.txt")
        self.account2 = BankAccount(balance=500)

    def tearDown(self) -> None:
        if os.path.exists("transaction_log.txt"):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as file:
            return len(file.readlines())

    def test_deposit_increases_balance_by_deposit_amount(self):
        new_balance = self.account.deposit(100)
        # assert new_balance == 2100
        self.assertEqual(new_balance, 2100)

    @patch("src.bank_account.datetime")
    def test_deposit_decreases_balance_by_withdraw_amount(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 11, 10)
        new_balance = self.account.withdraw(500)
        # assert new_balance == 1500
        # self.assertEqual(new_balance, 1501, "Balance is not equal")
        self.assertEqual(new_balance, 1500)

    def test_get_balance_returns_current_balance(self):
        # assert self.account.get_balance() == 2000
        self.assertEqual(self.account.get_balance(), 2000)

    def test_transfer_with_sufficient_funds(self):
        new_balance = self.account.transfer(200, self.account2)
        self.assertEqual(new_balance, 1800)
        assert self.account2.get_balance() == 700

    def test_transfer_negative_or_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.transfer(-200, self.account2)

    def test_deposit_logs_transaction(self):
        self.account.deposit(100)
        # assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_withdraw_logs_each_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(100)
        assert self._count_lines(self.account.log_file) == 2

    def test_transfer_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.transfer(2500, self.account2)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussiness_hours(self, mock_datetime):
        # mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value = datetime(2024, 11, 11, 10)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 1900)

    @patch("src.bank_account.datetime")
    def test_withdraw_outside_bussiness_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 20
        with self.assertRaises(WithdrawTimeRestrictionError):
            self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 2000)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussiness_days(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 11, 10)
        self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_outside_bussiness_days(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 10, 10)
        with self.assertRaises(WithdrawDayRestrictionError):
            self.account.withdraw(100)

    def test_deposit_multiple_amounts(self):
        test_cases = [
            {"amount": 2100, "expected": 4100},
            {"amount": 100, "expected": 2100},
            {"amount": 4000, "expected": 6000},
            {"amount": 500, "expected": 2500},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=2000, log_file="transaction_log.txt")
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])
