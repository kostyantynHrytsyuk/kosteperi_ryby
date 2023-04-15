from banking import AccountHolder, BankAccount, Transfer

# Create some account holders
holder1 = AccountHolder("Alice", "555-1234", 25)
holder2 = AccountHolder("Bob", "555-5678", 30)
assert holder1.age == 25
assert holder1.name == "Alice"
assert holder1.phone == "555-1234"
assert isinstance(holder1, AccountHolder)
assert isinstance(holder2, AccountHolder)
assert str(holder1) == 'Name: Alice\nAge: 25\nPhone number: 555-1234'
assert str(holder2) == 'Name: Bob\nAge: 30\nPhone number: 555-5678'
assert holder1 != holder2


# Create some bank accounts
#name, phone, age, pin, balance, account_number
account1 = BankAccount("Alice", "555-1234", 25, "1234", 1000, '0998877665')
assert isinstance(account1, AccountHolder)
assert isinstance(account1, BankAccount)

assert account1.balance == 1000
#when we initialize class BankAccount account_number must contains only 10 numbers if not program stops.!!!!!!
assert account1.account_number == '0998877665'

# assert BankAccount.account_number == 100001
#when we create new object BankAccount account_number + 1
account2 = BankAccount("Bob", "555-5678", 30, "5678", 500, '0987543276')
# Also account must have transaction history
# assert BankAccount.account_number == 100002

assert isinstance(account2, AccountHolder)
assert isinstance(account2, BankAccount)

# Test getting pincode
assert account1.pincode == '1234'
assert account2.pincode == '5678'

# Test getting balance
# get_balance("password")
assert account1.get_balance("1234") == 1000
assert account2.get_balance("5678") == 500

# you have only 2 attempts enter password from different card(from different object)
assert account1.get_balance("0000") == "You enter incorrect password. You have only 1 attempts to enter the password!"
assert account1.get_balance("0000") == "You enter incorrect password. You have only 0 attempts to enter the password!"
try:
    account2.get_balance("0000")
except ValueError as e:
    assert str(e) == "Sorry but your card is blocked"

# Test changing PIN code
assert account1.pincode == "1234"
account1.pincode = "5678"
assert BankAccount.is_valid_pincode("5678") == True # if it is True you may change password
assert account1.pincode == "5678"

account1.pincode = "123" 
# assert BankAccount.is_valid_pincode("123") == 'Sorry but you must create good password!'
try:
    BankAccount.is_valid_pincode("123") # Password is not correct!.Password is not changed.
except AccountError as e:
    assert str(e) == 'Sorry but you must create good password!'
assert account1.pincode == "5678" # Password is not changed



transaction1 = Transfer("Bob", "555-5678", 30, "5678", 500, '0987543276')
assert Transfer.credit_money == 10000

# Test adding money
transaction1.add_money(500, "5678") # adding money for your account
assert transaction1.balance == 1000 # also add your operation(string) to history
assert transaction1.transaction_history[-1] == "Operation is done successfully!"
try: # your pin must be correct, balance more than 100 and amount is integer
    transaction1.add_money(10000, "5678")
except ValueError as e:
    assert str(e) == "Please check your password or maybe your amount is too much!"

# Test credit money
# also age must be more 18
assert transaction1.balance == 11000
transaction1.credit(1000, "5678")
assert transaction1.balance == 12000
assert transaction1.transaction_history[-1] == "Credit money 1000"
assert Transfer.credit_money == 9000 

transaction1.credit(10000, "5678")
assert transaction1.get_balance("5678") == 12000
assert transaction1.transaction_history[-1] == "Operation is not done. Please check your balance"
try:
    transaction1.get_balance("0000")
except ValueError as e:
    assert str(e) == "Sorry but your card is blocked"
assert transaction1.transaction_history[:2] == ['Operation is done successfully!', 'Operation is done successfully!']


transaction2 = Transfer("Bobik", "543-5678", 1, "1234", 500, '0987543254')
try: 
    transaction2.credit(1000, "1234")
except AccountError as e:
    assert str(e) == "You don`t have opportunity to recive this money!"
assert transaction2.transaction_history == []


# Test sending money to another account
transaction1.send_money(1000, account2, "5678")
assert transaction1.balance == 11000
assert account2.get_balance("5678") == 1500
assert transaction1.transaction_history[-1] == "You transfer money into account_number 0987543276"

try:
    transaction1.send_money(1000, account2, "567") #inccorect password
except AccountError as e:
    assert str(e) == "You cannot do this operation!"

try:
    transaction1.send_money(2000000000, account2, "567") # you not have much money
except AccountError as e:
    assert str(e) == "You cannot do this operation!"
