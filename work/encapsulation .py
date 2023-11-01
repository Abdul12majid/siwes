# encapsulation
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.name}'s account balance: ${self.__balance}"


class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.bank_account = BankAccount(name)

    def make_deposit(self, amount):
        self.bank_account.deposit(amount)

    def make_withdrawal(self, amount):
        self.bank_account.withdraw(amount)

    def get_balance(self):
        return self.bank_account.get_balance()

    def __str__(self):
        return f"{self.name} ({self.phone_number}): {self.address}"


def main():
    # Create a new customer
    customer = Customer("Alice", "123 Main Street", "(123) 456-7890")

    # Deposit some money into the customer's account
    customer.make_deposit(100)

    # Withdraw some money from the customer's account
    customer.make_withdrawal(50)

    # Get the customer's account balance
    balance = customer.get_balance()

    # Print the customer's account balance
    print(f"Customer balance: ${balance}")

    # Create a second customer
    customer2 = Customer("Bob", "456 Elm Street", "(987) 654-3210")

    # Transfer money from customer's account to customer2's account
    customer.make_withdrawal(25)
    customer2.make_deposit(25)

    # Print the balances of both customers' accounts
    print(f"Customer 1 balance: ${customer.get_balance()}")
    print(f"Customer 2 balance: ${customer2.get_balance()}")


if __name__ == "__main__":
    main()
