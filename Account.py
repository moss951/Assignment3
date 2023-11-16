class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance): # constructor
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance

    def getAccountNumber(self): # get acocunt number
        return self._accountNumber
    
    def getAccountHolderName(self): # get account name
        return self._accountHolderName
    
    def getRateOfInterest(self): # get interest rate
        return self._rateOfInterest
    
    def getCurrentBalance(self): # get balance
        return self._currentBalance
    
    def setAccountHolderName(self, newName): # set a new account name
        self._accountHolderName = newName

    def setRateOfInterest(self, newRate): # set a new interest rate
        self._rateOfInterest = newRate

    def deposit(self, depositAmount): # deposit money to the account
        if depositAmount > 0: # the user should enter a positive number
            self._currentBalance += depositAmount
            return True # return True if the deposit went through
        else:
            return False # return False if the deposit didn't go through
    
    def withdraw(self, withdrawAmount): # withdraw money from the account
        self._currentBalance -= withdrawAmount
        return True
