from ChequingAccount import ChequingAccount
from SavingsAccount import SavingsAccount

class Bank:
    def __init__(self, bankName):
        self._bankName = bankName
        self._accounts = [
            ChequingAccount(1234, 'Bob', 0.04, 1000.0, 200), 
            ChequingAccount(1000, 'John', 0.05, 2000.0, 400), 
            ChequingAccount(4389, 'Jane', 0.06, 3000.0, 600), 
            SavingsAccount(3422, 'Bob', 0.1, 2500.0, 0), 
            SavingsAccount(8472, 'John', 0.2, 5000.0, 100), 
            SavingsAccount(3278, 'Jane', 0.3, 7500.0, 200)
        ]

    def openChequingAccount(self, accountNumber, accountName, accountInterest, accountBalance, accountOverdraft):
        self._accounts.append(ChequingAccount(accountNumber, accountName, accountInterest, accountBalance, accountOverdraft))

    def openSavingsAccount(self, accountNumber, accountName, accountInterest, accountBalance, accountMinBalance):
        self._accounts.append(SavingsAccount(accountNumber, accountName, accountInterest, accountBalance, accountMinBalance))
    
    def searchAccount(self, accountNumber):
        for a in self._accounts:
            if accountNumber == a.getAccountNumber():
                return a
            
        return False