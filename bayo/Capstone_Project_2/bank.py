import json
import os
from account import Account

class Bank:
    """
    Manages all accounts.
    Handles creation, deposits, withdrawals, and file persistence.
    """

    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.accounts = {}
        self.load_data()

    def load_data(self):
        """Load account data from JSON file (if it exists)"""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for acc_num, info in data.items():
                    self.accounts[acc_num] = Account(
                        acc_num,
                        info["name"],
                        info["balance"],
                        info["transactions"]
                    )

    def save_data(self):
        """Save all accounts to JSON file"""
        data = {acc: self.accounts[acc].to_dict() for acc in self.accounts}
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def generate_account_number(self):
        """Generate sequential account numbers"""
        if not self.accounts:
            return "10001"
        last_num = max(int(n) for n in self.accounts.keys())
        return str(last_num + 1)

    def create_account(self, name):
        acc_num = self.generate_account_number()
        self.accounts[acc_num] = Account(acc_num, name, 0)
        self.save_data()
        return acc_num

    def find_account(self, acc_num):
        return self.accounts.get(acc_num, None)

    def deposit(self, acc_num, amount):
        acc = self.find_account(acc_num)
        if acc:
            acc.deposit(amount)
            self.save_data()
            return True
        return False

    def withdraw(self, acc_num, amount):
        acc = self.find_account(acc_num)
        if acc:
            if acc.withdraw(amount):
                self.save_data()
                return True
            return False
        return False

    def generate_statement(self, acc_num):
        acc = self.find_account(acc_num)
        return acc.transactions if acc else None
