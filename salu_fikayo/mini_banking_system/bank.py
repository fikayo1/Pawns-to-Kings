#!/usr/bin/env py
""""""

import json
import os
import random

from account import Account


class Bank:
    def __init__(self):
        self.__data_file = "storage.json"
        if os.path.exists(self.__data_file):
            self.__accounts = self.load_data()
        else:
            self.__accounts = {}

    def create_account(self, email: str):
        if self.__accounts:
            for accounts in self.__accounts.values():
                if accounts.email == email:
                    return 400
        account_number = self.generate_acc_number()
        user_account = Account(email=email, account_number=account_number)
        self.save_data(user_account)
        return 201

    def find_account(self, account_number: int):
        if self.__accounts:
            return self.__accounts.get(account_number)
        return None

    def deposit(self, account_number: int, amount: float):
        userAccount = self.find_account(account_number)
        if userAccount:
            result = userAccount.deposit(amount)
            if result:
                self.save_data(userAccount)
                return result
            else:
                return 500
        return 404

    def withdraw(self, account_number: int, amount: float):
        userAccount = self.find_account(account_number)
        if userAccount:
            result = userAccount.withdraw(amount)
            if result:
                self.save_data(userAccount)
                return result
            else:
                return 400
        return 404

    def save_data(self, account: Account):
        self.__accounts[account.account_number] = account
        if not os.path.exists(self.__data_file):
            saved_data = {}
            saved_data[account.account_number] = account.to_dict()
            with open(self.__data_file, "w") as f:
                json.dump(saved_data, f, indent=4)
            return 200
        else:
            history = self.load_data()
            history[account.account_number] = account
            save_in_dict = {k: v.to_dict() for k, v in history.items()}
            with open(self.__data_file, "w") as f:
                json.dump(save_in_dict, f, indent=4)
            return 200

    def load_data(self):
        """Loads all account history from file storage"""
        if os.path.exists(self.__data_file):
            with open(self.__data_file, "r") as f:
                """If history exists, it is converted from dictionary to Account object"""
                try:
                    content = json.load(f)
                    return {int(k): Account(**v) for k, v in content.items()}
                except json.JSONDecodeError:
                    return {}
        return {}

    def generate_acc_number(self):
        """Generate account numbers"""
        while True:
            account_number = random.randint(1000, 9999)
            if account_number not in self.__accounts.keys():
                return account_number

    def generate_statement(self, account_number):
        user_account = self.find_account(account_number)
        if user_account:
            return user_account.transactions
        else:
            return 404

    def check_balance(self, account_number):
        user_account = self.find_account(account_number)
        if user_account:
            return user_account.balance
        return 404


python_bank = Bank()
print(python_bank.check_balance(8542))
print(python_bank.find_account(8542))
