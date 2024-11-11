from datetime import datetime
from src.exception import (
    WithdrawTimeRestrictionError,
    WithdrawDayRestrictionError,
    InsufficientFundsError,
)


class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Account created")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as file:
                file.write(f"{message}\n")

    def deposit(self, amount):
        """
        >>> account = BankAccount(balance=2000)
        >>> account.deposit(100)
        2100
        """
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        # Si datetime.now() esta en horario permitido:
        # """
        # >>> account = BankAccount(balance=2000, log_file="transaction_log.txt")
        # >>> account.withdraw(100)
        # 1900
        # """

        # Si datetime.now() esta fuera de horario:
        # """
        # >>> account = BankAccount(balance=2000)
        # >>> account.withdraw(100)
        # Traceback (most recent call last):
        # src.exception.WithdrawDayRestrictionError: Withdrawal not is allowed on weekends
        # """

        now = datetime.now()
        if now.hour < 8 or now.hour > 19:
            raise WithdrawTimeRestrictionError("Withdrawal not allowed at this time")
        if now.weekday() > 4:
            raise WithdrawDayRestrictionError("Withdrawal not is allowed on weekends")
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self):
        """
        >>> account = BankAccount(balance=2000)
        >>> account.get_balance()
        2000
        """
        self._log_transaction(f"Balance checked: {self.balance}")
        return self.balance

    def transfer(self, amount, account):
        # """
        # >>> account1 = BankAccount(balance=2000)
        # >>> account2 = BankAccount(balance=500)
        # >>> account1.transfer(100, account2)
        # 1900
        # >>> account2.get_balance()
        # 600
        # """
        if self.balance < amount:
            self._log_transaction("Insufficient balance")
            raise InsufficientFundsError("Insufficient balance")
        if amount <= 0:
            self._log_transaction("Amount must be greater than zero")
            raise ValueError("Amount must be greater than zero")
        self.withdraw(amount)
        self._log_transaction(
            f"Transferred {amount} to {account}. New balance: {self.balance}"
        )
        account.deposit(amount)
        return self.balance


# if __name__ == "__main__":
#     account = BankAccount(balance=2000, log_file="transaction_log.txt")
#     account.withdraw(100)
