class Account:
    def __init__(self):
        self.name = ''
        self.number = 0
        self.balance = 0.0
        self.transactions = {}

class Bank:
    def __init__(self):
        self.accounts = {}   #dictionary to store accounts by number
        self.load_accounts() #load accounts from bank.json

    def add_account(self, name, number):
        account = Account()
        account.name = name
        account.number = number
        account.balance = 0.0
        account.transactions = {}
        self.accounts[number] = account
        return account

    def find_account(self, number):
        # First check if account is already loaded in memory
        if number in self.accounts:
            return self.accounts[number]
        
        # If not in memory, try to load from JSON file
        try:
            with open('bank.json', 'r') as f:
                content = f.read().strip()
                
            if content:
                # Parse the JSON content
                accounts_data = self.parse_json_content(content)
                if str(number) in accounts_data:
                    acc_data = accounts_data[str(number)]
                    account = Account()
                    account.number = number
                    account.name = acc_data['name']
                    account.balance = acc_data['balance']
                    account.transactions = acc_data['transactions']
                    
                    # Add to memory for future access
                    self.accounts[number] = account
                    return account
        except FileNotFoundError:
            print("No accounts file found.")
        except Exception as e:
            print(f"Error loading account {number}: {e}")
        
        return None

    
   


    def save_accounts(self):
        
        for acc_num, account in self.accounts.items():
            bank_data = ({
                "name": f"{account.name}",
                "number": account.number,
                "balance": account.balance,
                "transactions": account.transactions
            })
        print(bank_data)
        # Convert the account data to a JSON string
        json_data = dict_to_json_string(bank_data)

        with open("bank.json", 'a') as file:
            file.write("{" + str(json_data) + "}" + "\n") #writing the bank data unto the json file
        print('Accounts saved successfully.')

    def load_accounts(self):
        try:
            with open("bank.json", 'r') as file:
                content = file.read().strip()
                ...
        except FileNotFoundError:
            print("No existing accounts found. Starting fresh.")
            


def dict_to_json_string(bank_data):
    #converting python dict to JSON string
    json_str = str(bank_data).replace("'", '"')
    json_str = json_str.replace("True", "true").replace("False", "false")
    json_str = json_str.replace("None", "null")
    json_str = json_str.replace("{", "").replace("}", "")
    return json_str


account_number = []

def create_account(bank):
    account = Account()
    account.name = input('Name: ')
    account.number = len(account_number) + 1
    account_number.append(account.number)
    account.transactions = {}
    bank.add_account(account.name, account.number)
    print(f'Account created successfully! Your account number is {account.number}.')
    bank.save_accounts()
    return account

def add_transaction(account, type, amount):
    tx_id = len(account.transactions) + 1
    account.transactions[tx_id] = {
        'amount': amount,
        'type': type
    }

def deposit(bank, number, amount):
    account = bank.find_account(number)
    account.balance += amount
    add_transaction(account, 'deposit', amount)
    print(f'Deposited {amount}. New balance is {account.balance}.')
    print(account.transactions)

def withdraw(bank, number, amount):
    account = bank.find_account(number)
    account.balance -= amount
    add_transaction(account, 'withdraw', amount)
    print(f'Withdrew {amount}. New balance is {account.balance}.')

def get_balance(account):
    return account.balance



def main():
    bank = Bank()
    while True:
        print("\nWelcome to Mini Bank")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account = create_account(bank)
            #bank.accounts[account.number] = account
        elif choice == '2':
            acc_num = int(input("Enter your account number: "))
            if acc_num in account_number:
                amount = float(input("Enter amount to deposit: "))
                deposit(bank, acc_num, amount)
            else:
                print("Account not found.")
        elif choice == '3':
            acc_num = int(input("Enter your account number: "))
            if acc_num in account_number:
                amount = float(input("Enter amount to withdraw: "))
                withdraw(bank, acc_num, amount)
            else:
                print("Account not found.")
        elif choice == '4':
            acc_num = int(input("Enter your account number: "))
            if acc_num in account_number:
                balance = get_balance(bank.accounts[acc_num])
                print(f"Your balance is {balance}.")
            else:
                print("Account not found.")
        elif choice == '5':
            print("Thank you for using Mini Bank!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()