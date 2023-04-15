"""Implementation by Sofia Shuliak"""

#Я та Дзвенислава розробляли ідею разом, але через різну імплементацію вирішили, 
# що краще написати просто різні асерти і розглядати як два варіанти задачі

class AccountHolder:
    """
    Class that contains info about person that has account
    Info: name, phone, age
    """
    def __init__(self, name:str, phone:str, age:int) -> None:
        self.name = name
        self.phone = phone
        self.age = self.verify_age(age)

    def verify_age(self, age):
        """Age verification"""
        if isinstance(age, int) and age >= 14:
            return age
        else:
            raise AccountError("Wrong age")

    def __str__(self) -> str:
        return f"Name: {self.name}\nAge: {str(self.age)}\nPhone number: {self.phone}"
    
class AccountError(Exception):
    """Error for cases that consern account"""
    pass
class TransactionError(Exception):
    """transaction errors"""
    pass
    
class BankAccount(AccountHolder):
    """
    Class that contains info about account
    Info: pin, balance, account holder(name), account number
    """
    account_number_bank = 0

    def __init__(self, pin, balance, account_holder:AccountHolder, account_number:str, account_credit_limit:int) -> None:
        self.__pin = self.is_valid_pincode(pin)
        self.balance = balance
        self.account_holder  = account_holder
        BankAccount.account_number_bank  += 1
        self.account_number_bank  = BankAccount.account_number_bank
        self.account_number = self.check_account_number(account_number)
        self.transaction_history = []
        if not isinstance(account_credit_limit, int) or account_credit_limit < 0:
            raise AccountError('Credit limit is positive integer')
        else:
            self.account_credit_limit = account_credit_limit

    def get_balance(self, pin):
        """return balance if PIN is correct"""
        res = self.verify_pin(pin)
        return self.balance if res is True else AccountError('Wrong pin!')

    @property
    def get_pin(self):
        return self.__pin

    def is_valid_pincode(self, pin):
        """validates PIN"""
        if isinstance(pin, str) and len(pin) == 4 and pin.isdigit():
            return pin
        else:
            raise AccountError("Expression can't be pin")

    def verify_pin(self, pin):
        """Verifies PIN"""
        return self.__pin == pin

    def change_pin(self, new_pin):
        """Changes PIN"""
        self.__pin = new_pin

    def check_account_number(self, account_number):
        """Checks account number"""
        if isinstance(account_number, str) is True and len(account_number) == 10 and account_number.isdigit():
            return True
        else:
            raise TypeError('Wrong account number!')


class Transfer(BankAccount):
    bank_credit_limit = 1000000

    def __init__(self, pin, balance, account_holder: AccountHolder,  account_number:str, account_credit_limit) -> None:
        super().__init__(pin, balance, account_holder, account_number, account_credit_limit)


    def add_money(self, pin, amount):
        """
        Add money to account method
        """
        if self.verify_pin(pin) is False:
            raise TransactionError("Wrong PIN!")
        if not isinstance(amount, int) or amount <= 0:
            raise TransactionError("Amount of money should be a positive integer")

        self.balance += amount
        self.transaction_history.append(f"Current balance: {str(self.balance)}")
        return True


    def credit(self, amount):
        """
        method for taking credit money
        """
        if self.account_holder.age < 18:
            raise TransactionError('User should reach age of 18 to take credit money')
        if not isinstance(amount, int) or amount <= 0:
            raise TransactionError("Amount of money shuld be a positive integer")
        if self.account_credit_limit < amount:
            raise TransactionError('Limit is used')
        if Transfer.bank_credit_limit < amount:
            raise TransactionError('Bank limit is used')

        if self.balance < 5000:
            raise TransactionError('Not enough money')

        self.balance += amount
        Transfer.bank_credit_limit -= amount
        self.account_credit_limit -= amount
        self.transaction_history.append(f"Current balance: {str(self.balance)}")
        return True


    def send_money(self, pin, amount):
        """
        Method for extracting money from account
        Error also raised if holder is too young
        """
        if not isinstance(amount, int) or amount <= 0:
            raise TransactionError("Amount of money shuld be a positive number")
        if self.account_holder.age < 18 and amount > 10000:
            raise TransactionError("Transaction is too big for your age!")
        if self.verify_pin(pin) is False:
            raise TransactionError("Wrong pin!")
        if self.balance < amount:
            raise TransactionError("Not enough money!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Current balance: {str(self.balance)}")
            return True

def test_classes():
    """Asserts for testing"""

    holder1 = AccountHolder('August Bern', '+38 077 450 98 02', 22)
    assert holder1.name == "August Bern"
    assert holder1.phone == "+38 077 450 98 02"
    assert holder1.age == 22
    assert str(holder1) == "Name: August Bern\nAge: 22\nPhone number: +38 077 450 98 02"



    # Account holder should be a person that reached age of 14
    # Otherwise AccountError raises
    try:
        holder = AccountHolder('August Bern', '+38 077 450 98 02', 10)
        assert False
    except AccountError:
        assert True

    assert type(holder1)==AccountHolder
    assert isinstance(holder1, AccountHolder)


    bank_acc = BankAccount('4567', 5000, holder1, '4768089764', 10000)
    assert type(bank_acc) == BankAccount
    assert isinstance(bank_acc, BankAccount)
    assert bank_acc.verify_pin('4678') is False
    # PIN should be private variable

    # variable that saves amount of created accounts
    assert BankAccount.account_number_bank == 1
    bank_acc.change_pin('5638')
    assert bank_acc.verify_pin('5638') is True


    holder2 = AccountHolder('Anya Rook', '+38 077 568 90 01', 16)
    bank_acc2 = BankAccount("1111", 40000, holder2, "1223456789", 10000)

    assert BankAccount.account_number_bank == 2
    
    # Number of account must contain ONLY 10 digits
    # Otherwise TypeError should be raised
    try:
        b_acc =  BankAccount("1111", 40000, holder2, "089767", 10000)
        assert False
    except TypeError:
        assert True

    # PIN should be a string with ONLY 4 numbers in it
    # Otherwise AccountError should be raised
    try:
        acc = BankAccount(7695, 5000, holder1, '4768089764', 10000)
        assert False
    except AccountError:
        assert True




    transact = Transfer('5638', 5000, holder1, '4768089764', 10000)

    assert transact.send_money('5638', 2000) is True
    assert transact.get_balance('5638') == 3000


    assert transact.add_money('5638', 4000) is True
    assert transact.get_balance('5638') == 7000

    # Each account has its transaction history (list)
    # It updates every time when person sends money, takes credit, adds money
    assert transact.transaction_history == ["Current balance: 3000", "Current balance: 7000"]

    assert transact.credit(7000) is True
    assert transact.get_balance('5638') == 14000

    assert transact.send_money('5638', 6000) is True
    assert transact.send_money('5638', 1000) is True
    assert transact.transaction_history == ["Current balance: 3000", "Current balance: 7000", "Current balance: 14000", "Current balance: 8000", "Current balance: 7000"]


    transact2 = Transfer("1111", 40000, holder2, "1223456789", 10000)

    # Minors should have limits in sums of money they send. In our case it is 10000
    try:
        transact2.send_money("1111", 30000)
        assert False
    except TransactionError:
        assert True

    # PIN is also checked
    try:
        transact2.send_money("1456" ,100)
        assert False
    except TransactionError:
        assert True
    
    # You can't send more than you have on account
    try:
        transact2.send_money("1111" ,500000)
        assert False
    except TransactionError:
        assert True



    # Method add money checks PIN and amount of money too
    try:
        transact.add_money('2675', 4000)
        assert False
    except TransactionError:
        assert True

    try:
        transact.add_money('5638', -4000)
        assert False
    except TransactionError:
        assert True

    try:
        transact.add_money('5638', 4.50)
        assert False
    except TransactionError:
        assert True

    # There are two types of credit limits: account_credit_limit is for account
    # bank_credit_limit is amount of money bank can give on the whole
    try:
        transact.credit(4500)
        assert False
    except TransactionError:
        assert True

    try:
        transact.credit(50000)
        assert False
    except TransactionError:
        assert True

    
    assert transact.credit(1000) is True
    assert transact.account_credit_limit == 2000
    assert Transfer.bank_credit_limit == 992000

    assert transact.get_balance('5638') == 8000

    assert transact.send_money('5638', 4000) is True
    assert transact.get_balance('5638') == 4000


    accc = AccountHolder('Mark Tran', '945729573', 35)
    b_aaa = BankAccount('2222', 40000, accc, '1234567890', 300000000)
    tran = Transfer('2222', 40000, accc, '1234567890', 300000000)
    
    # Drained bank limits example

    try:
        tran.credit(1000000)
        assert False
    except TransactionError:
        assert True



    # To take credit, person should have at least 5000 on balance
    try:
        transact.credit(7000)
        assert False
    except TransactionError:
        assert True


    assert transact.add_money('5638', 2500) is True

    # Credit money can be give to people that reached age of 18
    # Otherwise TypeError should be raised
    try:
        transact2.credit(1000)
        assert False
    except TransactionError:
        assert True

    print('Done!')



if __name__ == "__main__":
    test_classes()
