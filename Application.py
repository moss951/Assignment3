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
        print('Number of accounts:', len(bank._accounts))

        userInput = input('Select account (enter account number), or enter \'e\' to go back to the main menu. ')

        if userInput.lower() == 'e':
            return

        try:
            accountNumber = int(userInput)
        except:
            print('Invalid input. Enter a number from 1 to', len(bank._accounts))
            continue

        if accountNumber < 1 or accountNumber > len(bank._accounts):
            print('Invalid input. Enter a number from 1 to', len(bank._accounts))
            continue

        showAccountMenu(bank, accountNumber)
            

def showAccountMenu(bank, accountNumber):
    accountIndex = accountNumber - 1

    while True:
        userInput = input('Select operation (enter corresponding number). 1: Display balance. 2: Deposit money. 3: Withdraw money. 4: Back to account menu. ')

        if userInput == '1':
            print('Current Balance:', bank._accounts[accountIndex].getCurrentBalance())
        elif userInput == '2':
            bank._accounts[accountIndex].deposit()
        elif userInput == '3':
            bank._accounts[accountIndex].withdraw()
        elif userInput == '4':
            return
        else:
            print('Invalid input.')
            
    
bank = Bank('RBC')

showMainMenu(bank)