import Account

class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super.__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraftLimit = overdraftLimit

    def withdraw(self):
        return
