import sys
import time
from bank import Bank
from customer import Customer
import tkinter
import re


customers_file = "customers.txt"
staff_file = "staff.txt"


class Banking:

    """
        A GUI app to represent the workings of a bank.

        It is very simple to use and can scaled up well
    """

    def __init__(self):
        #create the main window
        self.main_window = tkinter.Tk()

        self.bank = Bank("XYZ ltd.")
        self.main_frame = tkinter.Frame(self.main_window)
        self.sign_in_frame = tkinter.Frame(self.main_window)

        #create label for welcome message
        self.welcome = tkinter.Label(self.main_frame,text=f"Hello! welcome to {self.bank._name}")

        #create button for signing up
        self.sign_up = tkinter.Button(self.sign_in_frame,text="Sign Up",command=self.register)
        self.sign_up.pack(side="left")
        self.quit_button = tkinter.Button(self.sign_in_frame,text="Quit",command=self.main_window.destroy)
        self.quit_button.pack()

        self.sign_in_frame.pack()

        self.welcome.pack(side="left")
        self.main_frame.pack()

        tkinter.mainloop()

    def register(self):
        self.register_window = tkinter.Tk()
        self.register_frame = tkinter.Frame(self.register_window)
        self.message = tkinter.Label(self.register_frame,text="Sign up to get started")
        
        #create frame and label plus entry widgets for getting credientials
        self.name_frame = tkinter.Frame(self.register_window)
        self.name_label = tkinter.Label(self.name_frame,text="Enter your name")
        self.name_entry = tkinter.Entry(self.name_frame)

        self.email_frame = tkinter.Frame(self.register_window)
        self.email_label = tkinter.Label(self.email_frame,text="Enter your e-mail")
        self.email_entry = tkinter.Entry(self.email_frame)

        self.password_frame = tkinter.Frame(self.register_window)
        self.password_label = tkinter.Label(self.password_frame,text="Enter your password")
        self.password_entry = tkinter.Entry(self.password_frame)

        self.confirm_frame = tkinter.Frame(self.register_window)
        self.confirm_label = tkinter.Label(self.confirm_frame,text="confirm your password")
        self.confirm_entry = tkinter.Entry(self.confirm_frame)

        self.submit_frame = tkinter.Frame(self.register_window)
        self.submit_button = tkinter.Button(self.submit_frame,text="Sign Up",command=self.sign_in)


        #packing the frames and entries and labels
        self.name_frame.pack()
        self.name_entry.pack(side="right")
        self.name_label.pack(side="left")

        self.email_frame.pack()
        self.email_entry.pack(side="right")
        self.email_label.pack(side="left")

        self.password_frame.pack()
        self.password_entry.pack(side="right")
        self.password_label.pack(side="left")

        self.confirm_frame.pack()
        self.confirm_entry.pack(side="right")
        self.confirm_label.pack(side="left")

        self.submit_frame.pack()
        self.submit_button.pack(side="left")


    #get all the text from entry
    def sign_in(self):
        self.name = self.name_entry.get()
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()
        self.confirm = self.confirm_entry.get()

        #checks if password works and email is correct
        if self.validate_password(self.password) and self.validate_email(self.email):
            if self.password == self.confirm:
                with open(customers_file,"a") as file:
                    file.write(self.name + " " + self.email + " " + self.password)
                self.success = tkinter.Label(self.register_frame,text="Sign up successful!")
                self.success.pack()
            else:
                raise ValueError("Passwords do not match. password must have capital letters, lower case letters and numbers")
        else:
            raise ValueError("Enter your email and password in correct format")

    @staticmethod
    def validate_password(password: str) -> bool:
        valid = re.compile(r"[A-Za-z0-9]{6,}")
        if valid.match(password):
            return True
        return False

    @staticmethod
    def validate_email(email: str) -> bool:
        valid = re.compile(r"(\w)+(\d)*(\@)(\w){3,}(\.)(\w){3}")
        if valid.match(email):
            return True
        return False

# def do_banking(customers_file: str,staff_file: str) -> None:
#     """simulates a banking process"""
#     start = 0
#     end = 0
#     elapsed = 0
#     customer = None
#     if register(customers_file):
#         start = time.time()
#     bank.prompt()
#     answer = int(input(">>"))
#     #checks if answer supplied is 1, if so, account is created
#     if answer == 1:
#         customer = bank.create_account()
#         customer_file = open(customers_file,"a")
#         customer_file.write(f"{customer._name} {customer._acct_type} {customer._email} {customer._balance} {customer._acct_no}")
#         customer_file.close()
#         print(f"Your account number is {customer._acct_no}")
#         print()
#         bank.prompt()          #prompts again if user wants to check details or log out
#         res = int(input(">>"))
#         if res == 1:
#             print("you are already logged in.")
#         elif res == 2:
#             details = bank.check_details(customer._acct_no,customers_file)
#             if details:
#                 print(customer)
#                 bank.prompt()
#             else:
#                 print("account numbers do not match")
#         else:
#             print("log out successful.")
#             end = time.time()
#             elapsed = end - start
#             session = open("session.txt","w")
#             session.write(f"session started at {time.ctime(start)} and ended at {time.ctime(end)}. total elapsed time is {elapsed}secs\n")
#             session.close()
#     #here the answer is 2, details are printed
#     elif answer == 2:
#         details = bank.check_details(customer._acct_no,customers_file)
#         if details:
#             print(customer)
#             print()
#             bank.prompt()
#         else:
#             print("account number do not match with the one we have")
#     #here, the user has logged out
#     else:
#         print("successfully logged out. ")
#         print("1 Login \n2 Close app (1 for log in, 2 for closing)")
#         response = int(input(">>"))
#         if response == 1:
#             do_banking(customers_file,staff_file)
#         else:
#             sys.exit()


# def register(customers_file: str) -> bool:
#     """performs registration for staffs of bank."""
#     status = bank.is_registered(customers_file)
#     if status:
#         print("Log in successful.\n")
#         return status
#     else:
#         print("Log in failed, please try again.")
#         return False


# def transfer(sender: Customer,receiver: Customer,amount: float) -> None:
#     bank.make_transfer(sender,receiver,amount)

# def banking(customers_file,staff_file) -> None:
    # print(f"Hello. Welcome to {bank._name}. would you like to")
    # print("1 Login \n2 Close app (1 for log in, 2 for closing)")
    # response = int(input(">>"))
    # #begins the whole program if the response is 1
    # if response == 1:
    #     do_banking(customers_file,staff_file)
    # else:
    #     sys.exit()

if __name__ == "__main__":
    new = Banking()