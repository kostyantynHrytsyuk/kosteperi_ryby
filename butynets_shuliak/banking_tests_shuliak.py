
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
