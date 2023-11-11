class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance

    def getAccountNumber(self):
        return self._accountNumber
    
    def getAccountHolderName(self):
        return self._accountHolderName
    
    def getRateOfInterest(self):
        return self._rateOfInterest
    
    def getCurrentBalance(self):
        return self._currentBalance
    
    def setAccountHolderName(self, newName):
        self._accountHolderName = newName

    def setRateOfInterest(self, newRate):
        self._rateOfInterest = newRate

    def deposit(self):
        return
    
    def withdraw(self):
        return
