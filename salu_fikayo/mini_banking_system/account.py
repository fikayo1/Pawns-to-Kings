#!/usr/bin/env py
"""This module contains the structure of the account class"""

import json
from datetime import datetime


class Account:
    __number_of_accounts = 0

    def __init__(self, name: str, **kwargs) -> None:
        """Initializes every instance of the Account class"""
        if not kwargs:
            self.name = name
            self.balance = 0.00
            self.transactions = []
            Account.__number_of_accounts += 1
            self.account_number = 1000 + Account.__number_of_accounts
        else:
            self.name = kwargs.get("name", "")
            self.balance = kwargs.get("balance", 0.0)
            self.transactions = kwargs.get("transactions", None)
            self.account_number = kwargs.get("account_number", None)

    def deposit(self, amount: float) -> bool:
        """Adds money to the users account when deposited"""
        if amount:
            transaction = {
                "type": "deposit",
                "amount": amount,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            self.balance += amount
            self.transactions.append(transaction)
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """When the user withdraws money from the account"""
        if amount is float:
            if self.balance >= amount:
                self.balance -= amount
                transaction = {
                    "type": "withdrawal",
                    "amount": amount,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                }
                self.transactions.append(transaction)
                return True
        return False

    @property
    def get_balance(self):
        """Returns the user's account balance"""
        return self.balance

    def to_dict(self):
        """Returns a dictionary of the instance"""
        accountObj: dict = self.__dict__
        if accountObj["account_number"]:
            del accountObj["account_number"]
        return accountObj

    def __str__(self):
        return f"{self.__dict__}"


acc1 = Account("salu")
acc2 = Account("lawal")
Output = acc1.deposit(23)
Output = acc1.deposit(23.34)
Output = acc1.deposit(34)
print(json.dumps(acc1.to_dict()))
print(acc2)
