from Bank import Bank

def run():
    return

def showMainMenu(bank):
    while True:
        userInput = input('Select operation (enter corresponding number). 1: Select Account. 2: Open Account. 3: Exit. ')

        if userInput == '1':
            selectAccountMenu(bank)
        elif userInput == '2':
            bank.openAccount()
        elif userInput == '3':
            break
        else:
            print('Invalid input.')

def selectAccountMenu(bank):
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

        # get account index
        accountIndex = None

        for i in range(len(bank._accounts)):
            if accountNumber == bank._accounts[i].getAccountNumber():
                accountIndex = i
                break
        
        if accountIndex is None:
            print('Invalid input. Enter a valid account number.')
            continue

        showAccountMenu(bank, accountIndex)

def showAccountMenu(bank, accountIndex):
    while True:
        userInput = input('Select operation (enter corresponding number). 1: Display balance. 2: Deposit money. 3: Withdraw money. 4: Back to account menu. ')

        if userInput == '1':
            print('Current Balance:', bank._accounts[accountIndex].getCurrentBalance())
        elif userInput == '2':
            userInput = input('Enter deposit amount: ')

            try:
                depositAmount = float(userInput)
            except:
                print('Invalid input. Enter a number.')
                continue

            bank._accounts[accountIndex].deposit(depositAmount)
            print('Deposit was successful.')
        elif userInput == '3':
            userInput = input('Enter withdraw amount: ')

            try:
                withdrawAmount = float(userInput)
            except:
                print('Invalid input. Enter a number.')
                continue

            if not bank._accounts[accountIndex].withdraw(withdrawAmount):
                print('Withdraw failed.')
            else:
                print('Withdraw was successful.')
        elif userInput == '4':
            return
        else:
            print('Invalid input.')
            
    
bank = Bank('RBC')

showMainMenu(bank)