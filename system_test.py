import unittest

from customer import Customer
from bank import Bank
from atm import ATM

# class TestBank(unittest.TestCase):

#     def test_register_with_good_value(self):
#         bank = Bank("xyz")
#         self.assertEqual(True,bank.register())

#     def test_details(self):
#         bank = Bank("xyz")
#         user = Customer("xyz","savings","xyz.com",500000,"4357697834")
#         self.assertEqual(True,bank.check_details(user.acct_no))


class TestCustomer(unittest.TestCase):

    def test_transfer(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(50000,user.transfer(50000))

    def test_transfer_with_negative_value(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(0,user.transfer(-50000))

    def test_transfer_with_value_too_high(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(0,user.transfer(50000000))

    def test_withdraw(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(50000,user.withdraw(50000))

    def test_withdraw_with_negative_value(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(0,user.transfer(-50000))

    def test_withdraw_with_value_too_high(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(0,user.transfer(50000000))



class TestATN(unittest.TestCase):

    def test_withdrawal(self):
        atm = ATM()
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(50000,atm.withdraw(user,50000))

    def test_withdrawal_with_negative_value(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        atm = ATM()
        self.assertEqual(0,atm.withdraw(user,-50000))

    def test_balance_check(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        atm = ATM()
        self.assertEqual(500000,atm.check_balance(user))

    def test_check_acct_no(self):
        atm = ATM()
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(user.acct_no,atm.check_acct_no(user))

    def test_airtime_purchase(self):
        atm = ATM()
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(5000,atm.buy_airtime(user,5000))

    def test_airtime_purchase_with_negative_value(self):
        atm = ATM()
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(0,atm.buy_airtime(user,-5000))

    def test_airtime_purchase_with_value_too_high(self):
        atm = ATM()
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        self.assertEqual(0,atm.buy_airtime(user,5000000000))

    def test_pin_generation(self):
        user = Customer("xyz","savings","xyz.com",500000,"4357697834")
        atm = ATM()
        self.assertEqual(2000,atm.generate_pin(user))




if __name__ == "__main__":
    unittest.main()