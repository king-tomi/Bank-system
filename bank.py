import random
from customer import Customer
from atm import ATM
from enum import Enum
import time
from datetime import date
import os
from typing import Tuple
 
class Bank:
    """A class to simulate a banking system.
    
    provides different static methods that models the functions of a bank
    
    Author: Tomisin Ayodabo
    
    Date Created: 8 May, 2020
    
    Date Modified: 11 May, 2020"""

    current = os.getcwd()
    class LOAN(Enum):
        AGRIC = 0.30
        MQ = 0.31
        OG = 0.31
        MANUFACTURING = 0.31
        REC = 0.31
        GENERAL = 0.31
        MORTGAGE = 0.31
        TC = 0.31
        GOVT = 0.30

    def __init__(self,name: str):
        self._name = name

    @staticmethod
    def is_registered(filename: str) -> bool:
        #this allows the user to register by checking the inputs given
        #to the values in the file.
        #returns true if successfully logged in else False
        Bank.current = os.path.join(Bank.current,filename)
        with open(Bank.current,"r") as file:
            user_name = input("Enter username: ")
            password = input("Enter password: ")
            staffs = file.readlines()
            found = False
            while not found:
                for staff in staffs:
                    credentials = staff.split(" ")
                    if user_name == credentials[0] and password == credentials[1]:
                        found = True
            return found

    @staticmethod
    def create_account() -> Customer:
        #this creates an account and returns a customer object
        name = input("Enter name of account: ")
        balance = float(input("Enter the opening balance: "))
        acnt_type = input("Enter account type(savings or current): ")
        email = input("Enter account email: ")
        acnt_no = "".join([str(random.randint(0,9)) for _ in range(10)])
        bank = input("Enter the bank name: ")
        customer = Customer(name,acnt_type,email,balance,acnt_no,500000,bank)
        return customer

    @staticmethod
    def logout(des: str) -> bool:
        return True if des == "yes" else False

    @staticmethod
    def check_details(acct_no: str,filepath: str) -> bool:
        #checks if account number supplied is in the customer file
        customer = ""
        with open(filepath,'r') as customers:
            cust_list = customers.readlines()
            found = False
            while not found:
                for cus in cust_list:
                    if acct_no == cus.split(" ")[4]:
                        customer += cus
                        found = True
            return found

    @staticmethod
    def prompt():
        print("1 Create new bank account \n\n2 Check Acount Details \n\n3 Logout")

    @staticmethod
    def make_transfer(customer: Customer,receiver: Customer,amount: float):
        """transfer is done through the ATM class"""
        ATM.transfer(customer,receiver,amount)

    @staticmethod
    def take_loan(user: Customer,amount: float,loan_type: str):
        """This allows users to take loans according to the type of the loanself.
        
        attr:
        
        user: An instace of the Customer class
        
        loan_type: the type of loan as defined in the LOAN enum. it resolves to a rate"""
        try:
            if loan_type in Bank.LOAN.__members__.keys():
                print("Your loan is processing, please wait...")
                loan = Bank.LOAN[loan_type].value * amount + amount    #interest is the first expression.
                user.balance = user.balance + loan
                time.sleep(5)
                today = date.today()
                print(f"Loan processing successful. amount has been added to your balance as at {today}")
            else:
                print("The loan you are applying for is not part of the ones we offer. please check again")
        except TypeError:
            print("There was an error, please try again later")

    @staticmethod
    def generate_receipt(name: str ,acct_no: int, amount: Tuple[float,int], transact_type: str="P"):
        """Generates reports for customer based on the type of transaction carried out
        
           Input:
                 name -> name of customer : str
                 
                 acct_no -> account number of customer -> int
                 
                 amount -> amount of money processed -> float or int
                 
                 transact_Type -> the type of transaction -> str
                        P for payment
                        W for withdrawal
        """
        current = time.time()
        if transact_type == "P":
            with open("payment.txt","a") as file:
                file.write(f"Customer name: {name}\n")
                file.write(f"Account_no: {str(acct_no)[7:]}\n")
                file.write(f"Amount paid: {amount}")
                file.write(f"Date of Transaction: {date.today()}")
                file.write(f"Time of Transaction: {time.localtime(current)}")
        elif transact_type == "W":
            with open("withdraw.txt","a") as file:
                file.write(f"Customer name: {name}\n")
                file.write(f"Account_no: {str(acct_no)[7:]}\n")
                file.write(f"Amount withdrawed: {amount}")
                file.write(f"Date of Transaction: {date.today()}")
                file.write(f"Time of Transaction: {time.localtime(current)}")
        else:
            return None
