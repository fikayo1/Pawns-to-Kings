#!/usr/bin/env py
""""""

import json
import os

from account import Account


class Bank:
    def __init__(self):
        self.__accounts: list[Account] = []
        self.__data_file = "storage.json"

    def create_account(self, name):
        userAccount = Account(name)
        self.__accounts.append(userAccount)

    def find_account(self, account_number):
        for item in self.__accounts:
            if account_number == item.account_number:
                return item
            else:
                return None

    def deposit(self, account_number, amount):
        userAccount = self.find_account(account_number)
        if userAccount:
            result = userAccount.deposit(amount)
            return result
        return None

    def withdraw(self, account_number, amount):
        userAccount = self.find_account(account_number)
        if userAccount:
            result = userAccount.withdraw(amount)
            return result
        return None

    def save_data(self, data: dict):
        if not os.path.exists(self.__data_file):
            savedData = {}
            savedData[data["account_number"]] = data.to_dict()
            with open(self.__data_file, "w") as f:
                json.dump(savedData, f, indent=4)
            return data.to_dict()

    def load_data(self):
        if os.path.exists(self.__data_file):
            with open(self.__data_file, "r") as f:
                content: dict[int:Account] = json.loads(f.read())
            return content
        return None

    def generate_statement(self):
        pass
