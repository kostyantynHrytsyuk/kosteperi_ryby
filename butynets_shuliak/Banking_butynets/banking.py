"""
Module banking
"""
class AccountHolder:
    """
    Info about Account`s holder
    """
    def __init__(self, name, phone, age) -> None:
        """
        Initialize class AccountHolder
        """
        self.name = name
        self.phone = phone
        self.age = age

    def __str__(self) -> str:
        """
        Returns this string
        """
        return f"Name: {self.name}\nAge: {self.age}\nPhone number: {self.phone}"
    
class AccountError(Exception):
    """Error for cases that consern both transactions and age limits"""
    pass

class BankAccount(AccountHolder):
    account_number_bank = 100000
    pin_attempt = 2

    def __init__(self, name, phone, age, pin, balance, account_number) -> None:
        super().__init__(name, phone, age)
        """
        Initialize class BankAccount
        """
        self.__pin = pin
        self.balance = balance
        self.account_number  = BankAccount.check_account_number(account_number)
        BankAccount.account_number_bank += 1
        self.transaction_history = []

    def get_balance(self, pincode:str) -> int:
        """
        Get account`s balance, check if correct pin-code returns balance else return string error
        """
        if pincode == self.pincode:
            return self.balance 
        else:
            if BankAccount.pin_attempt > 0:
                BankAccount.pin_attempt -= 1
                return f"You enter incorrect password. You have only \
{BankAccount.pin_attempt} attempts to enter the password!"
            else:
                raise ValueError("Sorry but your card is blocked")

    @property
    def pincode(self):
        """
        Recives your pin-code
        """
        return self.__pin
    
    @pincode.setter
    def pincode(self, new_password:str) -> None:
        if BankAccount.is_valid_pincode(new_password) is True:
            self.__pin = new_password
        
    @staticmethod
    def is_valid_pincode(pincode:str) -> bool:
        """
        Testing password to account
        """
        return True if isinstance(pincode, str) and len(pincode) == 4 and \
            pincode.isdigit() else AccountError('Sorry but you must create good password!')

    @staticmethod
    def check_account_number(account_number):
        """
        Check if account_number is correct
        """
        if len(account_number) == 10 and account_number.isdigit():
            return account_number
        else:
            raise TypeError("account_number is not correct!")

class Transfer(BankAccount):

    credit_money = 10000

    def __init__(self, name, phone, age, pin, balance, account_number) -> None:
        super().__init__(name, phone, age, pin, balance, account_number)

    def add_money(self, amount:int, pin_code:str):
        """
        Top up the card
        """
        if self.balance > 100 and isinstance(amount, int) and pin_code == self.pincode:
            self.balance += amount
            self.transaction_history.append(f"Operation is done successfully!")
        else:
            raise ValueError("Please check your password or maybe your amount is too much!")

    def credit(self, amount: int, pincode:str):
        """
        Give some credit money
        """
        if self.age < 18:
            raise AccountError("You don`t have opportunity to recive this money!")
        
        elif self.balance > 5000 and pincode == self.pincode and Transfer.credit_money - amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Credit money {amount}')
            Transfer.credit_money -= amount
        else:
            self.transaction_history.append(f'Operation is not done. Please check your balance')

    
    def send_money(self, amount, account: object, pincode:str):
        """
        Sending money to another account
        """
        if  self.balance - amount > 0 and pincode == self.pincode:
            account.balance += amount
            self.balance -= amount
            self.transaction_history.append(f'You transfer money into account_number {account.account_number}')
        else:
            raise AccountError("You cannot do this operation!")

