from Bank import Bank

class Application:
    def getInputAsInt(self, userInput):
        try:
            return int(userInput)
        except:
            print('Invalid input. Enter an integer.')
            return False
        
    def getInputAsFloat(self, userInput):
        try:
            return float(userInput)
        except:
            print('Invalid input. Enter a float.')
            return False

    def getAccountNumbersString(self, bank):
        accountNumbersString = ''

        for a in bank._accounts:
            accountNumbersString += str(a.getAccountNumber()) + ' '

        return accountNumbersString

    def run(self, bank):
        self.showMainMenu(bank)

    def showMainMenu(self, bank):
        while True:
            userInput = input('Select operation (enter corresponding number). 1: Select Account. 2: Open Account. 3: Exit. ')

            if userInput == '1':
                self.selectAccountMenu(bank)
            elif userInput == '2':
                bank.openAccount()
            elif userInput == '3':
                break
            else:
                print('Invalid input.')

    def selectAccountMenu(self, bank):
        while True:
            print('Account numbers:', self.getAccountNumbersString(bank))

            # get specified account number
            userInput = input('Select account (enter account number), or enter \'e\' to go back to the main menu. ')

            if userInput.lower() == 'e':
                return
            
            accountNumber = self.getInputAsInt(userInput)

            if not accountNumber:
                continue

            # get account from account number
            seletedAccount = bank.searchAccount(accountNumber)

            if not seletedAccount:
                print('Invalid input. Enter an existing account number.')
                continue

            self.showAccountMenu(seletedAccount)

    def showAccountMenu(self, account):
        while True:
            userInput = input('Select operation (enter corresponding number). 1: Display balance. 2: Deposit money. 3: Withdraw money. 4: Back to account menu. ')

            if userInput == '1':
                print('Current Balance:', account.getCurrentBalance())
            elif userInput == '2':
                userInput = input('Enter deposit amount: ')

                depositAmount = self.getInputAsFloat(userInput)

                if not depositAmount:
                    continue

                if not account.deposit(depositAmount):
                    print('Deposit failed.')
                else:
                    print('Deposit was successful.')
            elif userInput == '3':
                userInput = input('Enter withdraw amount: ')

                withdrawAmount = self.getInputAsFloat(userInput)

                if not withdrawAmount:
                    continue

                if not account.withdraw(withdrawAmount):
                    print('Withdraw failed.')
                else:
                    print('Withdraw was successful.')
            elif userInput == '4':
                return
            else:
                print('Invalid input.')
            

app = Application()    
bank = Bank('RBC')

app.run(bank)