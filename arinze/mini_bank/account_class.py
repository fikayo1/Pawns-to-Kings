class Account:
    def __init__(self):
        self.name = ''  
        self.number = 0
        self.balance = 0.0
        self.transactions = {}

    def add_transaction(self, type, amount):
        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = {
            'type': type,
            'amount': amount
        }
        return self.transactions
    
    def deposit(self, amount):
        self.balance += amount
        self.add_transaction('deposit', amount)
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        self.add_transaction('withdraw', amount)
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def to_dict(self):
        return {
            'name': self.name,
            'number': self.number,
            'balance': self.balance,
            'transactions': self.transactions
        }

    