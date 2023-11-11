from ChequingAccount import ChequingAccount
from SavingsAccount import SavingsAccount

class Bank:
    def __init__(self, bankName):
        self._bankName = bankName
        self._accounts = [
            ChequingAccount(1234, 'Bob', 0.04, 1000, 200), 
            ChequingAccount(1000, 'John', 0.05, 2000, 400), 
            ChequingAccount(4389, 'Jane', 0.06, 3000, 600), 
            SavingsAccount(3422, 'Bob', 0.1, 2500, 0), 
            SavingsAccount(8472, 'John', 0.2, 5000, 100), 
            SavingsAccount(3278, 'Jane', 0.3, 7500, 200)
        ]

    def openAccount(self):
        return
    
    def searchAccount(self):
        return