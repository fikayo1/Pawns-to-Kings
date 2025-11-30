#!/usr/bin/env py
"""
This module contains the start_app function used to execute the bank app
"""

from bank import Bank

menu = """
 Welcome to Python Bank!
 1. Create Account
 2. Deposit
 3. Withdraw
 4. Check Balance
 5. Transaction History
 6. Exit
 Choose an option:
 """


def start_app():
    """
    This function executes the bank application,
    based on the user's selected options
    """
    python_bank = Bank()

    while True:
        option = input(menu)

        match option:
            case "1":
                email = input("Please provide an email: ")
                status = python_bank.create_account(email)

                if status == 201:
                    print("Your account has been created successfully")
                else:
                    print(
                        "This email is already in use, please select option '1' and try another email"
                    )

            case "2":
                account_number_str = input("Please provide you account number: ")
                amount_str = input("How much would you like to deposit: ")
                try:
                    amount_float = float(amount_str)
                    account_number_float = float(account_number_str)
                    status = python_bank.deposit(account_number_float, amount_float)

                    if status == 404:
                        print("This account does not exist")
                    elif status == 500:
                        print("Please try again later")
                    else:
                        print(f"Deposit successful: {status}")

                except (TypeError, ValueError):
                    print(
                        "Please make sure your amount and account number input are numbers. Select option '2' and try again"
                    )

            case "3":
                account_number_str = input("Please provide you account number: ")
                amount_str = input("How much would you like to withdraw: ")
                try:
                    amount_float = float(amount_str)
                    account_number_float = float(account_number_str)
                    status = python_bank.withdraw(account_number_float, amount_float)

                    if status == 404:
                        print("This account does not exist")
                    elif status == 400:
                        account = python_bank.find_account(account_number_float)
                        print(
                            f"The specified amount is more than your current balance of {account.balance}"
                        )
                    else:
                        print(f"Deposit successful: {status}")

                except (TypeError, ValueError):
                    print(
                        "Please make sure your amount and account number input are numbers. Select option '3' and try again"
                    )

            case "4":
                try:
                    account_number = float(
                        input("Please provide your account number: ")
                    )
                    status = python_bank.check_balance(account_number)

                    if status == 404:
                        print("Account does not exist please try again")
                    else:
                        print(status)

                except (TypeError, ValueError):
                    print(
                        "Please make sure your account number input are numbers. Select option '4' and try again"
                    )

            case "5":
                try:
                    account_number = float(
                        input("Please provide your account number: ")
                    )
                    status = python_bank.generate_statement(account_number)

                    if status == 404:
                        print("Account does not exist please try again")
                    else:
                        print(status)

                except (TypeError, ValueError):
                    print(
                        "Please make sure your account number input are numbers. Select option '4' and try again"
                    )

            case "6":
                print("Thank you for banking with us")
                return

            case _:
                print("Please select a number from the provided options")


start_app()
