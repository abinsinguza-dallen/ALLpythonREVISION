from datetime import datetime as dt
from re import X

class Account:
    Account="PostBank"
    def __init__(self,account_number,account_name,):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdrawal=[]
        self.transaction_fee=100
        self.loan_balance=0

    def deposit(self,   amount):
        if amount<=0:
            return f"Deposit should be positive amount"
        else:
          self.balance+=amount
          transaction = {"amount":amount,"balance":self.balance,"narration":"You withdrew", "time":dt.now()}
          self.deposits.append(self.balance)
        return f"hello {self.account_name} you have deposited {amount} and you new balance is {self.balance}"  


    def withdraw(self,amount):
        total=amount+self.transaction_fee
        if amount<=0:
            return f"withdraw should be greater than zero"
        elif amount>self.balance:
            return f"your balance is {self.balance} you can't withdraw {amount}"    
        else: 
         self.balance-=total
        transaction = {"amount":amount,"balance":self.balance,"narration":"You withdrew", "time":dt.now()}
        self.withdrawal.append(transaction)
        # return f"hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance}"  
        return f"{dt.now()} Hello {self.account_name} you have successfully withdrawn {amount} account balance is {self.balance}"

    def deposit_statement(self):
        for b in self.deposits:
            print(b, end="\n")
    
    def withdrawals_statement(self):
        for withdrawal in self.withdrawal:
            print(withdrawal,end="\n")

    def account_balance(self):
       return f"Hello your account balance is {self.balance}"   

    def borrow(self,amount): 
        if self.deposit>10:
            return f"cant borrow"
        elif amount>100:
            amount=self.balance
            return f"{self.balance}"      

