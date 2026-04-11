class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            return f'this is new balance: {self.__balance}'
        
        else : return 'invalid amount'
    
    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
            return f'new balance: {self.__balance}'
        else:
            return 'insufficient balance'
              
    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def add_interest(self,rate):
        c_balance = self.get_balance()
        interest = c_balance*(rate/100)
        self.deposit(interest)
        return self.get_balance()
    
class CurrentAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        try:
            if amount <=-500:

    
    def getbalance(self):
        return self._BankAccount__balance

        a = BankAccount(0)
        print(a.get_balance())

        print(dir(a))

        print(getbalance(a))