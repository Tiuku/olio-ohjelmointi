class BankAccount:
    def __init__(self, bal, owner):
        self.__balance = bal
        self.__owner = owner

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: Insufficiet funds.")

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def __str__(self):
        return f""" Balance: {self.__balance} Owner: {self.__owner}"""
