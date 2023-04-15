class AccountHolder:
    def __init__(self, name, phone, age):
        self.name=name
        self.phone=phone
        self.age=age
    
    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nPhone number: {self.phone}'
    
class AccountError(Exception):
    pass

class BankAccount(AccountHolder):
    attempt=2
    def __init__(self, name, phone, age, pincode, balance, account_number):
        super().__init__(name, phone, age)
        self._pincode=pincode
        self.balance=balance
        self.account_number=account_number

    @property
    def pincode(self):
        return self._pincode
    
    @pincode.setter
    def pincode(self, pincode):
        if len(pincode)==4:
            self._pincode=pincode

    def get_balance(self, pincode):
        if self.pincode==pincode:
            return self.balance
        else:
            self.attempt-=1
            if self.attempt>=0:
                return f"You enter incorrect password. You have only {self.attempt} attempts to enter the password!"
            else:
                raise ValueError("Sorry but your card is blocked")
            
    @staticmethod
    def is_valid_pincode(pincode):
        if len(pincode)==4 and isinstance(pincode, str):
            return True
        else:
            return 'Sorry but you must create good password!'
        

class Transfer(BankAccount):

    credit_money = 10000

    def __init__(self, name, phone, age, pin, balance, account_number) -> None:
        super().__init__(name, phone, age, pin, balance, account_number)
        self.transaction_history=[]

    def add_money(self, amount, pin_code):
        if not (isinstance(amount, int) and pin_code == self.pincode and self.balance > 100):
                raise ValueError("Please check your password or maybe your amount is too much!")
        self.balance += amount
        self.transaction_history.append("Operation is done successfully!")

    def credit(self, amount, pincode):
        if self.age < 18:
            raise AccountError("You don`t have opportunity to recive this money!")
        
        if not isinstance(amount, int) or pincode != self.pincode:
            self.transaction_history.append(f"Operation is not done. Please check your balance")
            return
        
        if self.balance <= 5000 or Transfer.credit_money - amount < 0:
            self.transaction_history.append(f"Operation is not done. Please check your balance")
            return
        
        self.balance += amount
        self.transaction_history.append(f'Credit money {amount}')
        Transfer.credit_money -= amount

    def send_money(self, amount, account, pincode):
        if pincode != self.pincode:
            raise AccountError("You cannot do this operation!")
            
        if self.balance < amount:
            raise AccountError("You cannot do this operation!")
        
        self.balance -= amount
        account.balance += amount
        self.transaction_history.append(f"You transfer money into account_number {account.account_number}")
