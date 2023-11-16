from Account import Account

class ChequingAccount(Account): # inherit from Account
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit): # constructor
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance) # call parent constructor
        self._overdraftLimit = overdraftLimit

    def withdraw(self, withdrawAmount): # override the parent withdraw method
        if withdrawAmount > self._currentBalance + self._overdraftLimit and withdrawAmount > 0: # checks if the account dpes not enough money to go through with the transaction
            return False # return False if the transaction did not go through
        else:
            self._currentBalance -= withdrawAmount
            return True # return True if the transaction went through
