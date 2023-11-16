from Account import Account

class SavingsAccount(Account): # inherit from Account
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance): # constructor
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance) # call parent constructor
        self._minimumBalance = minimumBalance

    def withdraw(self, withdrawAmount): # override parent withdraw method
        if self._currentBalance - withdrawAmount < self._minimumBalance and withdrawAmount > 0: # checks if the account dpes not enough money to go through with the transaction
            return False # return False if the transaction did not go through
        else:
            self._currentBalance -= withdrawAmount
            return True # return True if the transaction went through
