from account_class import Account
import json

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def create_account(self, name):
        account = Account()
        account.name = name
        account.number = len(self.accounts) + 1  # Simple increment for account number
        self.accounts[account.number] = account
        self.save_accounts()
        print(f"Account created for {name} with account number {account.number}.")
        return account
    
    def load_accounts(self):
        try:
            with open('bank.json', 'r') as f:
                content = f.read().strip()
                
            if content:
                accounts_data = json.loads(content)
                for acc_num, acc_info in accounts_data.items():
                    account = Account()
                    account.name = acc_info['name']
                    account.number = int(acc_num)
                    account.balance = acc_info['balance']
                    account.transactions = acc_info['transactions']
                    self.accounts[int(acc_num)] = account
        except Exception as e:
            print(f"Error loading accounts: {e}")

    def find_account(self, number):
        self.load_accounts()
        return self.accounts.get(number, None)
    
    def save_accounts(self):
        bank_data = {}
        for acc_num, account in self.accounts.items():
            bank_data[acc_num] = account.to_dict()
        
        try:
            with open('bank.json', 'w') as f:
                json.dump(bank_data, f, indent=4)
        except Exception as e:
            print(f"Error saving accounts: {e}")

    def deposit(self, number, amount):
        account = self.find_account(number)
        if account:
            account.deposit(amount)
            self.save_accounts()
            return account.get_balance()
        return None
    
    def withdraw(self, number, amount):
        account = self.find_account(number)
        if account:
            account.withdraw(amount)
            self.save_accounts()
            return account.get_balance()
        return None
    
    def generate_statement(self, number):
        account = self.find_account(number)
        if account:
            return account.to_dict()
        return None
    
    def get_account_number(self, num):
        Bank.load_accounts
        return 
