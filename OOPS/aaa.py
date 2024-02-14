class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

    def transfer_funds(self, recipient_account, amount):
        if amount > self.balance:
            print("Insufficient funds for transfer")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred {amount} to {recipient_account.owner_name}. Your current balance: {self.balance}")


# Example usage:
account1 = BankAccount("12345", "Alice", 1000)
account2 = BankAccount("54321", "Bob", 500)

account1.display_balance()
account2.display_balance()

account1.transfer_funds(account2, 300)

account1.display_balance()
account2.display_balance()
