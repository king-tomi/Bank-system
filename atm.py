import time
from customer import Customer

class ATM:
    """A class to model an ATM machine
    
    PS: It does not have a constructor"""

    @staticmethod
    def transfer(user: Customer,receiver: Customer,amount: float) -> None:
        """A method where a user is able to transfer a certain amount to another user
        
        both users are instances of the Customer class
        
        amount is a float""" 
        try:
            print("Please wait while your transaction is processing...")
            time.sleep(5)
            final = user.transfer(amount)
            if final > 0:
                receiver.balance = receiver.balance + final
                print(f"Transaction successful.N{amount} successfully transferred to {receiver.name}")
            else:
                print("Transaction not successful")
        except TypeError:
            print("An error occured")

    @staticmethod
    def withdraw(user: Customer,amount: float) -> float:
        return user.withdraw(amount)

    @staticmethod
    def check_balance(user: Customer) -> float:
        return user.balance

    @staticmethod
    def buy_airtime(user: Customer,amount: float) -> float:
        airtime = user.withdraw(amount)
        if airtime > 0:
            print("Airtime purchase successful.")
            return airtime
        else:
            print("Negative amount or insufficient balance")
            return 0

    @staticmethod
    def check_acct_no(user: Customer) -> str:
        return user.acct_no

    @staticmethod
    def generate_pin(user: Customer) -> int:
        pin = input("Enter Your preferred PIN number: ")
        if len(pin) > 4:
            print("PIN can not be more than four digits. please try again")
        time.sleep(3)
        print(f"PIN creation successful. Your pin is {pin}")
        return int(pin)