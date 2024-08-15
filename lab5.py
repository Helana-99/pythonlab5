# q1//////////////////

class Animal:
    def __init__(self, name, species, gender):
        self.name = name
        self.species = species
        self.gender = gender

    def make_sound(self):
        return f"{self.name} makes a sound."

    def describe(self):
        return f"{self.name} is a {self.species}."

    def eat(self):
        return f"{self.name} eats animal food."


class Cat(Animal):
    def __init__(self, name, gender):
        super().__init__(name, species="Cat", gender=gender)

    def meow(self):
        return f"{self.name} says Meow!"

    def eat(self):
        return f"{self.name} eats cat food."
# ////////////////////////////////////////////////////////////////////////////////////////////////////
# q2 

class BankAccount:
    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount cannot be negative")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def transfer_to(self, target_account, amount):
        if isinstance(target_account, BankAccount) and 0 < amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
        else:
            print("Transfer failed due to insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def generate_statement(self):
        return f"Account {self.account_number} balance: ${self.balance:.2f}"


class BankCustomer:
    def __init__(self, name, national_id, birth_date, address):
        self.name = name
        self.national_id = national_id
        self.birth_date = birth_date
        self.address = address
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, BankAccount):
            self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def get_total_balance(self):
        total_balance = sum(account.get_balance() for account in self.accounts)
        return total_balance

    def generate_customer_statement(self):
        statement = f"Customer: {self.name}\n"
        for account in self.accounts:
            statement += account.generate_statement() + "\n"
        statement += f"Total balance: ${self.get_total_balance():.2f}"
        return statement


class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.customers = []

    def add_customer(self, customer):
        if isinstance(customer, BankCustomer):
            self.customers.append(customer)

    def find_customer(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                return customer
        return None

    def transfer_between_accounts(self, source_account, target_account, amount):
        if isinstance(source_account, BankAccount) and isinstance(target_account, BankAccount):
            source_account.transfer_to(target_account, amount)
        else:
            print("Transfer failed due to invalid accounts.")
