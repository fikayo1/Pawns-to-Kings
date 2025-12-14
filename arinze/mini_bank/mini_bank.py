from bank_class import Bank
from account_class import Account


def main():
    bank = Bank()
    while True:
        print("\n")
        print("Welcome to Mini Bank!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Generate Account Report")
        print("6. Exit")
        choice = input("Choose an option numerically: ")
        if choice == '1':
            name = input("Enter your name: ")
            print(f"Confirm account creation for {name}? (y/n): ")
            confirm = input().lower()
            if confirm == 'y':
                bank.create_account(name)
            else:
                print("Account creation cancelled.")
        elif choice == '2':
            number = int(input("Enter account number: "))
            name = input("Type in account name for verification: ").lower()
            if name != bank.find_account(number).name.lower():
                print("Account name does not match. Transaction cancelled.")
                continue
            amount = float(input("Enter amount to deposit: "))
            balance = bank.deposit(number, amount)
            if balance is not None:
                print(f"Deposited {amount}. New balance: {balance}.")
            else:
                print("Account not found.")
        elif choice == '3':
            number = int(input("Enter account number: "))
            name = input("Type in account name for verification: ").lower()
            if name != bank.find_account(number).name.lower():
                print("Account name does not match. Transaction cancelled.")
                continue
            amount = float(input("Enter amount to withdraw: "))
            balance = bank.withdraw(number, amount)
            if balance is not None:
                print(f"Withdrew {amount}. New balance: {balance}.")
            else:
                print("Account not found.")
        elif choice == '4':
            number = int(input("Enter account number: "))
            name = input("Type in account name for verification: ").lower()
            if name != bank.find_account(number).name.lower():
                print("Account name does not match. Transaction cancelled.")
                continue
            account = bank.find_account(number)
            if account:
                print(f"Current balance: {account.get_balance()}.")
            else:
                print("Account not found.")
        elif choice == '5':
            number = int(input("Enter account number: "))
            name = input("Type in account name for verification: ").lower()
            if name != bank.find_account(number).name.lower():
                print("Account name does not match. Transaction cancelled.")
                continue
            account = bank.find_account(number)
            if account:
                print(f"Account Report for {account.name} (#{account.number}):")
                print(f"Balance: {account.get_balance()}")
                print("Transactions:")
                for tid, tinfo in account.transactions.items():
                    print(f"  ID: {tid}, Type: {tinfo['type']}, Amount: {tinfo['amount']}")
            else:
                print("Account not found.")
        elif choice == '6':
            print("Thank you for using Mini Bank. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()