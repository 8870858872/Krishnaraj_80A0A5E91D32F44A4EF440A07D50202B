class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}"

# Creating an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000.0)

# Testing deposit and withdrawal functionality
print(account.display_balance())  # Should display "Account Balance for John Doe: $1000.00"

# Depositing $500
if account.deposit(500):
    print("Deposit successful.")
else:
    print("Invalid deposit amount.")

# Withdrawing $200
if account.withdraw(200):
    print("Withdrawal successful.")
else:
    print("Insufficient funds or invalid withdrawal amount.")

print(account.display_balance())  # Should display "Account Balance for John Doe: $1300.00"