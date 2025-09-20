def check_balance(balance):
    """Show current balance."""
    print(f"\nYour current balance is: ₦{balance}\n")


def deposit(balance):
    """Deposit money into account."""
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"₦{amount} deposited successfully.")
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return balance


def withdraw(balance):
    """Withdraw money from account."""
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > balance:
                print("Insufficient balance. Try a smaller amount.")
            else:
                balance -= amount
                print(f"₦{amount} withdrawn successfully.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return balance


def main():
    balance = 1000  # starting balance

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

