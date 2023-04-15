import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account_holder = AccountHolder('tim', '123-456-7890', 25)

    def test_account_number(self):
        with self.assertRaises(TypeError):
            BankAccount('1234', 10000, self.account_holder, 12345678, 50000)
        with self.assertRaises(TypeError):
            BankAccount('1234', 10000, self.account_holder, 12345678900, 50000)

    def test_pin(self):
        with self.assertRaises(AccountError):
            BankAccount(1234, 10000, self.account_holder, 1234567890, 50000)
        with self.assertRaises(AccountError):
            BankAccount('123', 10000, self.account_holder, 1234567890, 50000)

    def test_verify_pin(self):
        self.bank_account = BankAccount('1234', 10000, self.account_holder, 1234567890, 50000)
        self.assertTrue(self.bank_account.verify_pin('1234'))
        self.assertFalse(self.bank_account.verify_pin('4321'))

    def test_change_pin(self):
        self.bank_account = BankAccount('1234', 10000, self.account_holder, 1234567890, 50000)
        self.bank_account.change_pin('4321')
        self.assertTrue(self.bank_account.verify_pin('4321'))

    def setUp(self):
        self.account_holder = AccountHolder('anna', '987-654-3210', 16)
        self.transfer = Transfer('5678', 5000, self.account_holder, 2345678901, 10000)

    def test_send_money(self):
        with self.assertRaises(TransactionError):
            self.transfer.send_money('5678', 6000)
        with self.assertRaises(TransactionError):
            self.transfer.send_money('5678', 9000)
        self.assertTrue(self.transfer.send_money('5678', 1000))
        self.assertEqual(self.transfer.balance, 4000)
        self.assertIn('Current balance: 4000', self.transfer.transaction_history)

    def test_acc_holder(self):
        holder = AccountHolder(name="Mary", phone="0987654321", age=20)
        self.assertEqual(holder.name, "Mary")
        self.assertEqual(holder.phone, "0987654321")
        self.assertEqual(holder.age, 20)

    def test_add_money(self):
        self.assertTrue(self.transfer.add_money('5678', 2000))
        self.assertEqual(self.transfer.balance, 7000)
        self.assertIn('Current balance: 7000', self.transfer.transaction_history)

    def test_get_balance(self):
        self.assertEqual(self.transfer.get_balance('5678'), 5000)


if __name__ == '__main__':
    unittest.main()
