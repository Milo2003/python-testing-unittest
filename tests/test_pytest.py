import pytest
from src.bank_account import BankAccount
from src.exception import (
    WithdrawTimeRestrictionError,
    WithdrawDayRestrictionError,
)
from unittest.mock import patch
from datetime import datetime


@pytest.fixture
def account():
    return BankAccount(balance=2000, log_file="transaction_log.txt")


@pytest.mark.parametrize(
    "amount, expected",
    [
        (1500, 3500),
        (100, 2100),
        (4000, 6000),
        (500, 2500),
    ],
)
def test_deposit_multiple_amounts(amount, expected, account):
    new_balance = account.deposit(amount)
    assert new_balance == expected


@pytest.mark.parametrize(
    "amount, expected_balance, should_raise",
    [
        (-100, 2000, True),  # Monto negativo que debería generar un ValueError
        (100, 2100, False),  # Monto positivo que debería incrementar el balance
    ],
)
def test_deposit_amount(amount, expected_balance, should_raise, account):
    if should_raise:
        with pytest.raises(ValueError):
            account.deposit(amount)
    else:
        new_balance = account.deposit(amount)
        assert new_balance == expected_balance


@patch("src.bank_account.datetime")
def test_withdraw_during_business_hours(mock_datetime, account):
    # Simula la hora en un momento laboral permitido (10:00 AM)
    mock_datetime.now.return_value = datetime(2024, 11, 11, 10)
    account.withdraw(100)
    assert account.get_balance() == 1900


@patch("src.bank_account.datetime")
def test_withdraw_outside_business_hours(mock_datetime, account):
    # Simula la hora fuera del horario laboral permitido (8:00 PM)
    mock_datetime.now.return_value = datetime(2024, 11, 11, 20)
    with pytest.raises(WithdrawTimeRestrictionError):
        account.withdraw(100)
    assert account.get_balance() == 2000


@patch("src.bank_account.datetime")
def test_withdraw_during_business_days(mock_datetime, account):
    # Simula un día laboral permitido (11 de noviembre de 2024)
    mock_datetime.now.return_value = datetime(2024, 11, 11, 10)
    account.withdraw(100)
    assert account.get_balance() == 1900


@patch("src.bank_account.datetime")
def test_withdraw_outside_business_days(mock_datetime, account):
    # Simula un día no laboral (domingo, 10 de noviembre de 2024)
    mock_datetime.now.return_value = datetime(2024, 11, 10, 10)
    with pytest.raises(WithdrawDayRestrictionError):
        account.withdraw(100)
    assert account.get_balance() == 2000


@pytest.mark.skip(reason="Not implemented yet")
def test_transfer_with_sufficient_funds(account):
    pass
