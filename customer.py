from enum import Enum,unique
from credit_card import CreditCard

class Customer:
    """A model class that represents a customer in a bank"""
    
    @unique
    class Max(Enum):
        """A nested class to hold the maximum deposit amounts for savings and current accounts"""
        SAVINGS = 300000.0
        CURRENT = 30000000.0

    def __init__(self,name: str,acct_type: str,email: str,balance: float,acct_no: str,credit: CreditCard,bank: str):
        self._name = name
        self._acct_type = acct_type
        self._email = email
        self._balance = balance
        self._acct_no = acct_no
        self._bank = bank
        self._limit = 200000000000.0
        self._credit = credit(self.name,self.bank,self.acct_no,self.balance,self._limit)

    def __str__(self):
        return f"{self._name} {self._acct_no} {self._acct_type} {self._balance}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value: str):
        self._name = value

    @property
    def acct_type(self):
        """The acct_type property."""
        return self._acct_type
    @acct_type.setter
    def acct_type(self, value: str):
        self._acct_type = value

    @property
    def email(self):
        """The email property."""
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def balance(self):
        """The balance property."""
        return self._balance

    @balance.setter
    def balance(self, value: float):
        self._balance = value

    @property
    def acct_no(self):
        """The acct_no property."""
        return self._acct_no

    @acct_no.setter
    def acct_no(self, value: str):
        self._acct_no = value

    @property
    def bank(self):
        return self._bank

    def transfer(self,amount: float) -> float:
        if 0 <= amount <= self.balance:
            self.balance = self.balance - amount
            return amount
        else:
            print("insufficient balance")
            return 0

    def withdraw(self,amount: float) -> float:
        return self.transfer(amount)

    def deposit(self,amount: float):
        """A user is allowed to deposit a certain amount according to the rules defined 
        by the Max enum class"""
        try:
            if self.acct_type == "savings":
                if amount > self.Max.SAVINGS:
                    print("Maximum deposit exceeded. please try again")
                else:
                    self.balance = self.balance + amount
            else:
                if amount > self.Max.CURRENT:
                    print("Maximum deposit exceeded. please try again")
                else:
                    self.balance = self.balance + amount
        except (TypeError,ValueError):
            print("An error occured")

    def change_acct_type(self,new_type: str):
        self.acct_type = new_type