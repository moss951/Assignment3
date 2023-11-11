from Bank import Bank

class Application:
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
            # print account numbers
            accountNumbersString = ''

            for a in bank._accounts:
                accountNumbersString += str(a.getAccountNumber()) + ' '

            print('Account numbers:', accountNumbersString)

            # get specified account number
            userInput = input('Select account (enter account number), or enter \'e\' to go back to the main menu. ')

            if userInput.lower() == 'e':
                return

            try:
                accountNumber = int(userInput)
            except:
                print('Invalid input. Enter a number.')
                continue

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

                try:
                    depositAmount = float(userInput)
                except:
                    print('Invalid input. Enter a number.')
                    continue

                if not account.deposit(depositAmount):
                    print('Deposit failed.')
                else:
                    print('Deposit was successful.')
            elif userInput == '3':
                userInput = input('Enter withdraw amount: ')

                try:
                    withdrawAmount = float(userInput)
                except:
                    print('Invalid input. Enter a number.')
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