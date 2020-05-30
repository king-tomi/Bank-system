import sys
import time
from bank import Bank

bank = Bank("XYZ ltd.")

def do_banking() -> None:
    """simulates a banking process"""
    start = 0
    end = 0
    elapsed = 0
    customer = None
    if register():
        start = time.time()
    bank.prompt()
    answer = int(input(">>"))
    #checks if answer supplied is 1, if so, account is created
    if answer == 1:
        customer = bank.create_account()
        customer_file = open("C:\\Users\\Tomisin Ayodabo\\Desktop\\dr charles\\customers.txt","a")
        customer_file.write(f"{customer._name} {customer._acct_type} {customer._email} {customer._balance} {customer._acct_no}")
        customer_file.close()
        print(f"Your account number is {customer._acct_no}")
        print()
        bank.prompt()          #prompts again if user wants to check details or log out
        res = int(input(">>"))
        if res == 1:
            print("you are already logged in.")
        elif res == 2:
            details = bank.check_details(customer._acct_no)
            if details:
                print(customer)
                bank.prompt()
            else:
                print("account numbers do not match")
        else:
            print("log out successful.")
            end = time.time()
            elapsed = end - start
            session = open("session.txt","w")
            session.write(f"session started at {time.ctime(start)} and ended at {time.ctime(end)}. total elapsed time is {elapsed}secs\n")
            session.close()
    #here the answer is 2, details are printed
    elif answer == 2:
        details = bank.check_details(customer._acct_no)
        if details:
            print(customer)
            print()
            bank.prompt()
        else:
            print("account number do not match with the one we have")
    #here, the user has logged out
    else:
        print("successfully logged out. ")
        print("1 Login \n2 Close app (1 for log in, 2 for closing)")
        response = int(input(">>"))
        if response == 1:
            do_banking()
        else:
            sys.exit()


def register() -> bool:
    """performs registration for staffs of bank."""
    status = bank.register()
    if status:
        print("Log in successful.\n")
        return status
    else:
        print("Log in failed, please try again.")
        return False


def transfer(sender: Customer,receiver: Customer,amount: float) -> None:
    bank.make_transfer(sender,receiver,amount)

def banking() -> None:
    print(f"Hello. Welcome to {bank._name}. would you like to")
    print("1 Login \n2 Close app (1 for log in, 2 for closing)")
    response = int(input(">>"))
    #begins the whole program if the response is 1
    if response == 1:
        do_banking()
    else:
        sys.exit()

banking()