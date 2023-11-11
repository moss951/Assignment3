from Account import Account

class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraftLimit = overdraftLimit

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self._currentBalance + self._overdraftLimit:
            return False
        else:
            self._currentBalance -= withdrawAmount
            return True
