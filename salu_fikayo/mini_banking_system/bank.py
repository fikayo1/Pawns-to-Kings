#!/usr/bin/env py
""""""

import json
import os

from account import Account


class Bank:
    def __init__(self):
        self.__accounts: dict[int:Account] = (
            {k: Account(**v) for k, v in self.load_data().items()}
            if os.path.exists(self.__data_file)
            else None
        )
        self.__data_file = "storage.json"

    def create_account(self, email: str):
        if not self.__accounts:
            user_account = Account(email)
            self.save_data(user_account)
            return 201
        else:
            for item in self.__accounts.values():
                if item.email == email:
                    return 401
            self.save_data(Account(email))
            return 201

    def find_account(self, account_number: int):
        if self.__accounts:
            for item in self.__accounts.keys():
                if account_number == item:
                    return self.__accounts.get(item)
            else:
                return None
        return None

    def deposit(self, account_number: int, amount: float):
        userAccount = self.find_account(account_number)
        if userAccount:
            result = userAccount.deposit(amount)
            if result:
                self.save_data(userAccount)
                return 200
            else:
                return 500
        return 404

    def withdraw(self, account_number: int, amount: float):
        userAccount = self.find_account(account_number)
        if userAccount:
            result = userAccount.withdraw(amount)
            if result:
                self.save_data(userAccount)
                return 200
            else:
                return 400
        return 404

    def save_data(self, data: Account):
        if not os.path.exists(self.__data_file):
            savedData = {}
            savedData[data["account_number"]] = data.to_dict()
            with open(self.__data_file, "w") as f:
                json.dump(savedData, f, indent=4)
            return data.to_dict()
        else:
            history: dict = self.load_data()
            for item in history.keys():
                if item == data.account_number:
                    history[item] = data.to_dict()

    def load_data(self):
        if os.path.exists(self.__data_file):
            with open(self.__data_file, "r") as f:
                content: dict[int:Account] = json.load(f)
            return content
        return None

    def generate_statement(self):
        pass


PythonBank = Bank()
PythonBank.create_account("salu@gmail.com")
