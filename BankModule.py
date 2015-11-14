import time
import os
from sys import stdout
from time import gmtime, strftime
from abc import ABCMeta,abstractmethod



class FullName(object):
    def __init__(self):
        self.first_name = raw_input("\nEnter your first name :")
        self.last_name = raw_input("\nEnter your last name :")
  

class AccountOperation(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def balance_query(self):
        pass


#===================================================================
#                       class BankAccount
#   this is the base class for all types of bank accounts
#   private member varialbes:
#                           account_number
#                           balance
#    member functions:
#                   create_account()
#                   withdraw()
#                   deposit()
#                   balance_query()
#                   show_info()
#==================================================================
class BankAccount(AccountOperation):
    def __init__(self):
        pass
    
    def create_account(self):
        self.__account_number = raw_input("Enter The account No. :")
        self.__balance = float(raw_input("Enter The Initial amount(>=0 for Saving and >=1500 for Checking): "))
    
    def withdraw(self):
        amount = float(raw_input("\tPlease enter the amount: "))
        self.__balance-=amount
        if self.__balance<amount:
            print "\tThe amount of money your are trying to withdraw exceed the current balance"
            return 0
        print "\tWithdraw Successfully at "+strftime("%Y-%m-%d %H:%M:%S", gmtime())
            
    def deposit(self):
        amount = float(raw_input("\tPlease enter the amount: "))
        self.__balance+=amount
        print "\tDeposit Successfully at "+strftime("%Y-%m-%d %H:%M:%S", gmtime())

    def balance_query(self):
        print "\tThe current balance: $"+"{0:.2f}".format(round(self.__balance,2))

    def show_info(self):
        print "\tAccount No. : "+str(self.__account_number)
        self.balance_query()

        
#==================================================================
#                       class CheckingAccount
#   this class is derived from the class BankAccount
#   additional private member varialbes:
#                                       __min_balance
#                                       __charge
#                                       __account_type
#   additional member functions:
#                               withdraw()
#                               transfer()
#==================================================================              
class CheckingAccount(BankAccount):
    def __init__(self):
        self.__min_balance = 1500.00
        self.__charge = 25.00

    def withdraw(self):
        amount = float(raw_input("\tPlease enter the amount: "))
        self._BankAccount__balance-=amount
        if self._BankAccount__balance<amount:
            print "\tThe amount of money your are trying to withdraw exceed the current balance"
            return 0
        if self._BankAccount__balance<self.__min_balance:
            self._BankAccount__balance-=self.__charge
            print "\tPlease keep your balance above the minmum balance, otherwise additional fee will be charged"
        print "\tWithdraw Successfully"
        
    def transfer(self,to_account):
        print "\tTransfer to the saving account"
        amount = float(raw_input("\tPlease enter the amount: "))        
        self._BankAccount__balance-=amount
        to_account._BankAccount__balance+=amount
        print "\tTransfer Succesfully "+strftime("%Y-%m-%d %H:%M:%S", gmtime())

#==================================================================
#                       class SavingAccount
#   this class is derived from the class BankAccount
#   private member varialbes:
#                           __annual_rate
#   additional member functions:
#                               transfer()
#==================================================================        
class SavingAccount(BankAccount):
    def __init__(self):
        self.__annual_rate = 0.1000
        
    def transfer(self,to_account):
        print "\tTransfer to the checking account"
        amount = float(raw_input("\tPlease enter the amount: "))        
        self._BankAccount__balance-=amount
        to_account._BankAccount__balance+=amount
        print "Transfer Succesfully "+strftime("%Y-%m-%d %H:%M:%S", gmtime())



#==================================================================
#                       class Client
#   private member varialbes:
#                            __name
#                            __account_reservoir  ## used to hold checking and saving accounts
#   additional  member functions:
#                           add_checking_account()
#                           add_saving_account()
#================================================================== 

class Client(object):        
    def __init__(self):
        self.__name = FullName()
        self._account_reservoir = {}
         
    def add_checking_account(self):
        print "\nADD A NEW CHECKING ACCOUNT"
        account = CheckingAccount()
        account.create_account()
        self._account_reservoir["checking"]=account        
        print "SUCCESSFULLY ADDED A CHECKING ACCOUNT!"
        
    def add_saving_account(self):
        print "\nADD A NEW SAVING ACCOUNT"
        account = SavingAccount()
        account.create_account()
        self._account_reservoir["saving"]=account 
        print "SUCCESSFULLY ADDED A SAVING ACCOUNT!"
       
        
#==================================================================
#                       class OnlineBanking
#   this class is a class for online banking system
#   member varialbes: client              
#   member functions:
#                   create_online_account()
#                   __login() (private)
#                   sign_in()
#==================================================================
class OnlineBanking(object):
    def __init__(self,client):
        self.client = client
        pass
        
    def create_online_account(self):
        os.system('cls')
        print "\n\n\n\t\t\tSign up for Online Banking Today!\n\n"
        self.onlineId = raw_input("OnlineId: ")
        self.passCode = raw_input("\nPasscode: ")
        print "YOU SUCCESSFULLY CREATE A ONLINE ACCOUNT!"
        
    def __login(self):       
        in_username = raw_input("Please Enter Username: ")
        in_password = raw_input("Please Enter Password: ")
        if(in_username==self.onlineId and in_password==self.passCode):
            time.sleep(2.0)
            print 'Logged in Successfully as '+ in_username
            time.sleep(1.0)
            return 1
        if (in_username!=self.onlineId or in_password!=self.passCode):
            print 'Invalid Username or Password, Try Again'+'\n'
            return 0

    def sign_in(self):
        os.system('cls')
        print "*"*70
        print "\t\t\t        PLEASE SIGN IN        \n\n"
        count = 3
        flag=0
        while (flag==0 and count>0):
            flag = self.__login()
            count-=1 
        if flag==0:
            print "Exceeded the login times"
            return 0
        return 1



#***********************************************************************
#    functions to display the main menu of the online banking system
#***********************************************************************
    
def display_main_menu(client):
    def exit_func():
        print "\n\nThanks for using online banking system"
        stdout.write('Signing out')
        t=10
        while t>0: 
            stdout.write('.') 
            t-=1
            time.sleep(0.5) 
        stdout.write('\n') 
    os.system('cls')
    print "\n"
    print "*"*70
    print "\n\tMAIN MENU"
    print "\n\n\t01. DISPLAY ACCOUNT INFO"
    print "\n\n\t02. DEPOSIT AMOUNT"
    print "\n\n\t03. WITHDRAW AMOUNT"
    print "\n\n\t04. TRANSFER AMOUNT"
    print "\n\n\t05. BALANCE ENQUIRY"
    print "\n\n\t06. EXIT\n"
    print "*"*70
    option = int(raw_input("\n\tSelect your option (1-6): "))
    if option==6:
        exit_func()
        return 0
    accountType = raw_input("\n\tSelect an account(checking/saving): ") 
    os.system('cls')
    account = client._account_reservoir[accountType]
    toAccountType = list(set(["checking","saving"])-set([accountType]))[0]
    toAccount = client._account_reservoir[toAccountType]
    accountAction={1: show_info,
                   2: deposit,
                   3: withdraw,
                   5: balance_query,
                  }
    if option==4:
        account.transfer(toAccount)
    if option!=4:
        accountAction[option](account)
    time.sleep(3.5)
    os.system('cls')
    return 1



def main_menu_loop(client):
    flag=1
    while flag!=0:
        flag = display_main_menu(client)
        
def show_info(account):
    return account.show_info()

def deposit(account):
    return account.deposit()

def withdraw(account):
    return account.withdraw()

def balance_query(account):
    return account.balance_query()


def continue_open(accountType,accountOpenOption):
    new_account_str = list(set(["checking","saving"])-set([accountType]))[0]     # get another account type
    continueOpen=raw_input("\nDo you want to continue to open a " + new_account_str+" account(Y/N)? ")
    if continueOpen=='Y':
        accountOpenOption[new_account_str]()
        time.sleep(2)
