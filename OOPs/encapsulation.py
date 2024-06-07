import os 
import sys 

class BankAccount():
    def __init__(self,account_id,balance=0) -> None:
        self.__balance__= balance
        self.__account_id__=account_id
    
    def get_account(self):
        return self.__account_id__
    
    def get_balance(self):
        return self.__balance__
    
    def set_balance(self,amount):
        if amount < 0:
            print("Invalid amount ")
        else:
            self.__balance__=amount
    
    def deposit(self,amount):
        if amount > 0 :
            #TODO explain this operation in future
            self.__balance__+=amount 
        else:
            print("Invalid amount for deposit")
    
    def withdraw(self,amount):
        if amount >0 and amount <= self.__balance__:
            self.__balance__-=amount 
        else:
            print("Invalida amount for withdraw")

    
    
    
if __name__=="__main__":
    setu_account = BankAccount("2410")
    divya_account = BankAccount("2905",1000)
    print(setu_account.get_balance(),divya_account.get_balance())
    setu_account.deposit(15000)
    divya_account.withdraw(500)
    print("after deposit and withdraw")
    print(setu_account.get_balance(),divya_account.get_balance())
    # setu_account.deposit("sdfsdf")
    setu_account.deposit(-100)
    divya_account.withdraw(45000)
    print("afrter 2nd deposit and withdraw")
    print(setu_account.get_balance(),divya_account.get_balance())

        