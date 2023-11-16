from Bank import Bank

class Application: # methods for user interaction
    def getInputAsInt(self, userInput): # convert the user's input into an integer
        try:
            return int(userInput)
        except:
            print('Invalid input. Enter an integer.')
            return False # any variable that was unsuccessfully casted to an int is be equal to False
        
    def getInputAsFloat(self, userInput): # convert the user's input into a float
        try:
            return float(userInput)
        except:
            print('Invalid input. Enter a float.')
            return False # any variable that was unsuccessfully casted to an int is be equal to False

    def getAccountNumbersString(self, bank): # get a string that contains all the bank's account numbers
        accountNumbersString = ''

        for a in bank._accounts:
            accountNumbersString += str(a.getAccountNumber()) + ' '

        return accountNumbersString

    def run(self, bank): # run the program
        self.showMainMenu(bank)

    def showMainMenu(self, bank): # display the main menu, which loops until the user decides to quit
        while True:
            userInput = input('Select operation (enter corresponding number). 1: Select Account. 2: Open Account. 3: Exit. ')

            if userInput == '1': # select account
                self.selectAccountMenu(bank)
            elif userInput == '2': # open account
                self.openAccountMenu(bank)
            elif userInput == '3': # exit
                break
            else:
                print('Invalid input.')

    def selectAccountMenu(self, bank): # select an account
        while True:
            print('Account numbers:', self.getAccountNumbersString(bank))

            # get specified account number
            userInput = input('Select account (enter account number), or enter \'e\' to go back to the main menu. ')

            if userInput.lower() == 'e':
                return
            
            accountNumber = self.getInputAsInt(userInput)

            if not accountNumber: # don't proceed until the user enters a valid account number
                continue

            # get account from account number
            seletedAccount = bank.searchAccount(accountNumber)

            if not seletedAccount: # don't proceed until an existing account number has been chosen. selectedAccount would be False after unsuccessfully finding an account
                print('Invalid input. Enter an existing account number.')
                continue

            self.showAccountMenu(seletedAccount)

    def openAccountMenu(self, bank): # makes a new account using the user's inputs as its arguments
        while True:
            userInput = input('Select account type. 1: Chequing Account. 2: Savings Account. 3: Exit. ')

            if userInput == '3':
                return

            accountType = self.getInputAsInt(userInput)
            # 'not accountType' refers to the accountType not successfully being casted to an int (it would return False)
            if not accountType or accountType < 1 or accountType > 2: # don't proceed until a valid account type has been chosen
                print('Enter a valid account type.')
                continue

            while True:
                accountNumber = self.getInputAsInt(input('Enter account number. '))

                if accountNumber == False: # don't proceed until an integer has been entered. 
                    continue
                
                isUniqueNumber = True
                for a in bank._accounts: # checks if the user's specified account number already exists by comparing it to every existing account number
                    if accountNumber == a._accountNumber:
                        print('This account number already exists.')
                        isUniqueNumber = False # this boolean is used to break out of the loop if a unique number has been entered, or loop again if an existing number has been entered
                        break

                if isUniqueNumber: # proceed if a unique account number has been entered
                    break

            accountName = input('Enter account name. ')

            while True:
                accountInterest = self.getInputAsFloat(input('Enter account interest. '))
                if accountInterest != False: # if the user's input was successfully converted to a float
                    break

            while True:
                accountBalance = self.getInputAsFloat(input('Enter account balance. '))
                if accountBalance != False: # if the user's input was successfully converted to a float
                    break

            if accountType == 1: # if the user wants to open a chequing account
                while True:
                    accountOverdraft = self.getInputAsFloat(input('Enter account overdraft limit. '))
                    if accountOverdraft != False: # if the user's input was successfully converted to a float
                        break

                bank.openChequingAccount(accountNumber, accountName, accountInterest, accountBalance, accountOverdraft)
            elif accountType == 2: # if the user wants to open a savings account
                while True:
                    accountMinBalance = self.getInputAsFloat(input('Enter account minimum balance. '))
                    if accountMinBalance != False: # if the user's input was successfully converted to a float
                        break

                bank.openSavingsAccount(accountNumber, accountName, accountInterest, accountBalance, accountMinBalance)


    def showAccountMenu(self, account): # display the account menu for account-related operations
        while True:
            userInput = input('Select operation (enter corresponding number). 1: Display balance. 2: Deposit money. 3: Withdraw money. 4: Back to account menu. ')

            if userInput == '1': # display current balance
                print('Current Balance:', account.getCurrentBalance())
            elif userInput == '2': # deposit money
                userInput = input('Enter deposit amount: ')

                depositAmount = self.getInputAsFloat(userInput)

                if not depositAmount: # don't proceed until the user entered a float
                    continue

                if not account.deposit(depositAmount): # run the deposit method. If it returns false, nothing will happen to the account's balance. If it returns true, that means the balance has been updated
                    print('Deposit failed.')
                else:
                    print('Deposit was successful.')
            elif userInput == '3': # withdraw money
                userInput = input('Enter withdraw amount: ')

                withdrawAmount = self.getInputAsFloat(userInput)

                if not withdrawAmount: # don't proceed until the user entered a float
                    continue

                if not account.withdraw(withdrawAmount): # run the withdraw method. If it returns false, nothing will happen to the account's balance. If it returns true, that means the balance has been updated
                    print('Withdraw failed.')
                else:
                    print('Withdraw was successful.')
            elif userInput == '4': # exit account menu
                return
            else:
                print('Invalid input.')
            

app = Application()    
bank = Bank('RBC')

app.run(bank)