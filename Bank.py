from ChequingAccount import ChequingAccount
from SavingsAccount import SavingsAccount

class Bank:
    def __init__(self, bankName):
        self._bankName = bankName
        self._accounts = [ChequingAccount(1, 'Bob', 0.05, 1000, 200), SavingsAccount(2, 'Bob', 0.1, 2500, 0)]

    def openAccount(self):
        return
    
    def searchAccount(self):
        return