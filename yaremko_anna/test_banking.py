import unittest
from banking import AccountHolder, BankAccount, Transfer


class TestBanking(unittest.TestCase):
    def test_account_holder(self):
        holder1 = AccountHolder("Alice", "555-1234", 25)
        holder2 = AccountHolder("Bob", "555-5678", 30)
        self.assertEqual(holder1.age, 25)
        self.assertEqual(holder1.name, "Alice")
        self.assertEqual(holder1.phone, "555-1234")
        self.assertIsInstance(holder1, AccountHolder)
        self.assertIsInstance(holder2, AccountHolder)
        self.assertEqual(str(holder1), 'Name: Alice\nAge: 25\nPhone number: 555-1234')
        self.assertEqual(str(holder2), 'Name: Bob\nAge: 30\nPhone number: 555-5678')
        self.assertNotEqual(holder1, holder2)

    def test_bank_account(self):
        account1 = BankAccount("Alice", "555-1234", 25, "1234", 1000, '0998877665')
        account2 = BankAccount("Bob", "555-5678", 30, "5678", 500, '0987543276')

        self.assertIsInstance(account1, AccountHolder)
        self.assertIsInstance(account1, BankAccount)
        self.assertEqual(account1.balance, 1000)
        self.assertEqual(account1.account_number, '0998877665')
        self.assertIsInstance(account2, AccountHolder)
        self.assertIsInstance(account2, BankAccount)
        self.assertEqual(account2.pincode, '5678')
        self.assertEqual(account2.get_balance("5678"), 500)

        self.assertEqual(account1.pincode, '1234')
        self.assertEqual(account2.pincode, '5678')

        self.assertEqual(account1.get_balance("1234"), 1000)
        self.assertEqual(account2.get_balance("5678"), 500)
        self.assertEqual(account1.get_balance("0000"), "You enter incorrect password. You have only 1 attempts to enter the password!")
        self.assertEqual(account1.get_balance("0000"), "You enter incorrect password. You have only 0 attempts to enter the password!")
        self.assertEqual(account1.pincode, "1234")
        account1.pincode = "5678"
        self.assertTrue(BankAccount.is_valid_pincode("5678"))
        self.assertEqual(account1.pincode, "5678")

    def test_transfer(self):
        transaction1 = Transfer("Bob", "555-5678", 30, "5678", 500, '0987543276')

        self.assertEqual(Transfer.credit_money, 10000)
        transaction1.add_money(500, "5678")
        self.assertEqual(transaction1.balance, 1000)
        self.assertEqual(transaction1.transaction_history[-1], "Operation is done successfully!")



if __name__ == '__main__':
    unittest.main()