import Account

class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super.__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._minimumBalance = minimumBalance

    def withdraw():
        return
