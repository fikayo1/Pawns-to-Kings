#!/usr/bin/env py
"""This module contains the logic for the bank class"""

import json
import os
import random

from account import Account


class Bank:
    """Establishes the logic for a banking system"""

    def __init__(self):
        """Initializes all bank instances with the specified attributes"""
        self.__data_file = "storage.json"
        if os.path.exists(self.__data_file):
            self.__accounts = self.load_data()
        else:
            self.__accounts = {}

    def create_account(self, email: str):
        """Creates a new account for a user with the specified email
        but returns "400" if the email already exists
        """
        if self.__accounts:
            for accounts in self.__accounts.values():
                if accounts.email == email:
                    return 400
        account_number = self.generate_acc_number()
        user_account = Account(email=email, account_number=account_number)
        self.save_data(user_account)
        return 201

    def find_account(self, account_number: int):
        """Checks if the account exists and returns it if it does"""
        if self.__accounts:
            return self.__accounts.get(account_number)
        return None

    def deposit(self, account_number: int, amount: float):
        """Deposits money to a user's account if the account exists"""
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
        """Withdraws the specified amount from the user's account"""
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
        """Saves any update to the storage file and the accounts dictionary"""
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
        """Loads all account history from the storage file"""
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
        """Generate random and unique account numbers for users"""
        while True:
            account_number = random.randint(1000, 9999)
            if account_number not in self.__accounts.keys():
                return account_number

    def generate_statement(self, account_number):
        """Generates the user's account statement based on transactions made"""
        user_account = self.find_account(account_number)
        if user_account:
            return user_account.transactions
        else:
            return 404

    def check_balance(self, account_number):
        """Returns the user's account balance and 404 if the account does not exist"""
        user_account = self.find_account(account_number)
        if user_account:
            return user_account.balance
        return 404
