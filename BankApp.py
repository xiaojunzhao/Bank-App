from BankModule import *
       
if __name__=='__main__':
    
    #===== Open a new account in our Banking System!========#
    print "*"*70
    print "\n\t\t WELCOME TO THE BANK SYSTEM\n"
    print "*"*70
    clientObj = Client()
    accountOpenOption = {'checking': clientObj.add_checking_account,
                         'saving': clientObj.add_saving_account
                         }     
    string = raw_input("\nWhat kind of bank account would you like to open (checking/saving)? ")
    new_str = string.strip() 
    accountOpenOption[new_str.lower()]()
    continue_open(new_str.lower(),accountOpenOption)
    
    #============= Log into Online Banking Today ==========#    
    account1 = OnlineBanking(clientObj)
    account1.create_online_account()
    signInFlag = account1.sign_in()
    if signInFlag==1:
        main_menu_loop(clientObj)
        

