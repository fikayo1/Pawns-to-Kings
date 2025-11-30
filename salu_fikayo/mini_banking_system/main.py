#!/usr/bin/env py
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
    python_bank = Bank()

    while True:
        option = float(input(menu))

        match option:
            case 1:
                email = input("Please provide an email: ")
                status = python_bank.create_account(email)

                if status == 201:
                    print("Your account has been created successfully")
                else:
                    print(
                        "This email is already in use, please select option '1' and try another email"
                    )
            case 2:
                account_number = input("Please provide you account number: ")
                amount_str = input("How much would you like to deposit: ")
                try:
                    amount_float = float(amount_str)
                    status = python_bank.deposit(account_number, amount_float)

                    if status != 404 or status != 500:
                        print(status)
                    elif status == 404:
                        print("This account does not exist")
                    else:
                        print("Please try again later")

                except (TypeError, ValueError):
                    print(
                        "Please make sure your amount input is a number. Select option '2' and try again"
                    )
            case 6:
                print("Thank you for banking with us")
                return
            case _:
                print("Please select a number from the provided options")


start_app()
