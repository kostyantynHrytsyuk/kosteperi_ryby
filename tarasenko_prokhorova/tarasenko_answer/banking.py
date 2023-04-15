"""a module for bank accounts"""
class AccountHolder:
    """a class for account holders"""
    def __init__(self, name, phone, age):
        self.name = name
        self.phone = phone
        self.age = age
        if age < 14:
            raise AccountError("Age must be at least 14")
    def __str__(self) -> str:
        return f'Name: {self.name}\nAge: {self.age}\nPhone number: {self.phone}'
class AccountError(Exception):
    """a class for account errors"""
    pass

class BankAccount:
    """a class for bank accounts"""
    account_number_bank = 0
    def __init__(self, pin, balance, account_holder: AccountHolder, \
account_number: int, account_credit_limit):
        self.__pin = pin
        self.balance = balance
        self.account_holder = account_holder
        self.account_number = account_number
        self.account_credit_limit = account_credit_limit
        BankAccount.account_number_bank += 1
        if len(str(account_number))!= 10:
            raise TypeError("Account number must be 10 digits")
        if not isinstance(self.__pin, str):
            raise AccountError
        elif len(self.__pin)!= 4:
            raise AccountError

    def verify_pin(self, pin):
        """a method for verifying a pin"""
        if self.__pin == pin:
            return True
        return False

    def change_pin(self, new_pin):
        """a method for changing a pin"""
        self.__pin = new_pin
class Transfer(BankAccount):
    """a class for transfers"""
    bank_credit_limit = 1000000
    def __init__(self, pin, balance, account_holder: \
AccountHolder, account_number: int, account_credit_limit):
        super().__init__(pin, balance, account_holder, account_number, account_credit_limit)
        self.transaction_history = []
    def send_money(self, pin, amount):
        '''a method for sending money'''
        if self.verify_pin(pin):
            if self.verify_pin(pin):
                if self.account_holder.age < 18:
                    if amount >= 10000:
                        raise TransactionError
            if amount <= self.balance:
                self.balance = self.balance - amount
                self.transaction_history.append(f"Current balance: {str(self.balance)}")
                return True
            raise TransactionError
        raise TransactionError

    def add_money(self, pin, amount):
        """a method for adding money"""
        if self.verify_pin(pin):
            if amount <= 10:
                raise TransactionError
            self.balance = self.balance + amount
            self.transaction_history.append(f"Current balance: {str(self.balance)}")
            return True
        raise TransactionError

    def get_balance(self, pin):
        """a method for getting balance"""
        if self.verify_pin(pin):
            return self.balance
    def credit(self, amount):
        """a method for crediting"""
        if self.account_holder.age < 18 or not isinstance(amount, int) or \
amount <= 0 or self.account_credit_limit < amount or Transfer.\
bank_credit_limit < amount or self.balance < 5000:
            raise TransactionError
        self.balance += amount
        Transfer.bank_credit_limit -= amount
        self.account_credit_limit -= amount
        self.transaction_history.append(f"Current balance: {self.balance}")
        return True

class TransactionError(Exception):
    """a class for transaction errors"""
    pass
