import datetime

class Account:
    """
    Represents a single bank account.
    Handles deposits, withdrawals, and transaction history.
    """

    def __init__(self, account_number, name, balance=0, transactions=None):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = transactions if transactions else []

    def deposit(self, amount):
        """Add money to balance"""
        self.balance += amount
        self.add_transaction("deposit", amount)

    def withdraw(self, amount):
        """Withdraw money (prevent overdraft)"""
        if amount > self.balance:
            return False  # failed
        self.balance -= amount
        self.add_transaction("withdrawal", amount)
        return True

    def add_transaction(self, type, amount):
        """Store transaction details with timestamp"""
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.transactions.append({
            "type": type,
            "amount": amount,
            "time": time_now
        })

    def get_balance(self):
        return self.balance

    def to_dict(self):
        """Convert object to dictionary for JSON saving"""
        return {
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }
