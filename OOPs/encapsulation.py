import os 
import sys 

class BankAccount():
    def __init__(self,personname,account_id) -> None:
        self.__personname__=personname
        self.__account_id__=account_id
    def getter_person(self):
        return self.__personname__
    def getter_account(self):
        return self.__account_id__
    def setter_account(self,new_accountid):
        self.__account_id__=new_accountid 
        return self.__account_id__
    
    
if __name__=="__main__":
    new_account = BankAccount("setu","123434545")
    print(new_account.getter_account())
    new_account.setter_account("2112121212")
    print(new_account.getter_account())
    

        