class BankAccount {
  String accountNumber;
  String ownerName;
  double balance;

  BankAccount(this.accountNumber, this.ownerName, {this.balance = 0});

  void deposit(double amount) {
    balance += amount;
    print("Deposited $amount. Current balance: $balance");
  }

  void withdraw(double amount) {
    if (amount > balance) {
      print("Insufficient funds");
    } else {
      balance -= amount;
      print("Withdrew $amount. Current balance: $balance");
    }
  }

  void displayBalance() {
    print("Account Number: $accountNumber, Balance: $balance");
  }

  void transferFunds(BankAccount recipientAccount, double amount) {
    if (amount > balance) {
      print("Insufficient funds for transfer");
    } else {
      balance -= amount;
      recipientAccount.balance += amount;
      print("Transferred $amount to ${recipientAccount.ownerName}. Your current balance: $balance");
    }
  }
}

void main() {
  var account1 = BankAccount("12345", "Alice", balance: 1000);
  var account2 = BankAccount("54321", "Bob", balance: 500);

  account1.displayBalance();
  account2.displayBalance();

  account1.transferFunds(account2, 300);

  account1.displayBalance();
  account2.displayBalance();
}
