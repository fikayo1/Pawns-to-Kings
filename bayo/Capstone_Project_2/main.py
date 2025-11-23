from bank import Bank

bank = Bank()

def menu():
    print("\n==================================")
    print("     WELCOME TO BAYO'S BANK")
    print("==================================")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        acc = bank.create_account(name)
        print(f"Account created successfully! Account Number: {acc}")

    elif choice == "2":
        acc = input("Enter account number: ")
        amt = int(input("Enter deposit amount: "))
        if bank.deposit(acc, amt):
            print("Deposit successful!")
        else:
            print("Account not found.")

    elif choice == "3":
        acc = input("Enter account number: ")
        amt = int(input("Enter withdrawal amount: "))
        if bank.withdraw(acc, amt):
            print("Withdrawal successful!")
        else:
            print("Failed. Insufficient funds or invalid account.")

    elif choice == "4":
        acc = input("Enter account number: ")
        account = bank.find_account(acc)
        if account:
            print(f"Balance: ₦{account.balance}")
            print("\nLast 5 transactions:")
            for t in account.transactions[-5:]:
                print(f"- {t['type']} {t['amount']} ({t['time']})")
        else:
            print("Account not found.")

    elif choice == "5":
        acc = input("Enter account number: ")
        history = bank.generate_statement(acc)
        if history:
            print("\n--- Transaction History ---")
            for t in history:
                print(f"{t['time']} | {t['type']} | ₦{t['amount']}")
        else:
            print("Account not found.")

    elif choice == "6":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Try again.")
