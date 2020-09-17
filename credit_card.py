class CreditCard:

    def __init__(self,name: str,bank: str,acnt : int,balance: float,limit: float):
        if self._validate_account_num(acnt):
            self._acnt = acnt
            self._name = name
            self._bank = bank
            self._balance = balance
            self._limit = limit
        else:
            raise ValueError("Account number greater than or less than 10 digits")

    @property
    def name(self):
        return self._name

    @property
    def bank(self):
        return self._bank

    @property
    def acnt(self):
        return self._acnt

    @property
    def balance(self):
        return self._balance

    @property
    def limit(self):
        return self._limit

    @staticmethod
    def _validate_account_num(account : int) -> bool:
        return len(str(account)) == 10

    def __str__(self):
        return f"{self.name} {self.bank}"