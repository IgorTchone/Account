class Account:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} completed. Current balance: {self.balance}\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} completed. Current balance: {self.balance}\n")
        else:
            print("Insufficient balance for withdrawal.\n")

    def display_balance(self):
        return f"Balance of {self.account_holder}: {self.balance}"

    def compare_balance(self, other_account):
        if self.balance > other_account.balance:
            return f"{self.account_holder} has more money than {other_account.account_holder}."
        elif self.balance < other_account.balance:
            return f"{other_account.account_holder} has more money than {self.account_holder}."
        else:
            return f"{self.account_holder} and {other_account.account_holder} have the same amount of money."

# Creating two accounts
if __name__ == "__main__":
    account1 = Account("Igor Riba", "123456789", 1000)
    account2 = Account("Lilian Spegiorin", "987654321", 1500)

    # Displaying the balances
    print(account1.display_balance() + "\n")
    print(account2.display_balance() + "\n")

    # Comparing the balances
    result = account1.compare_balance(account2)
    print(result + "\n")

    # Making a deposit in account1
    account1.deposit(500)

    # Making a withdrawal from account2
    account2.withdraw(200)

    # Comparing again
    result = account1.compare_balance(account2)
    print(result)