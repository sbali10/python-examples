#Atm application


SBAccount = {
    "name" : "Serhat Bali",
    "accountNumber" : "321",
    "limit" : 7500,
    "secondLimit" : 4500
}

BBAccount = {
    "name" : "Baran Bali",
    "accountNumber" : "456",
    "limit" : 8500,
    "secondLimit" : 3500
}

def moneyDraw(account, amount):
    print(f"Hello, {account['name']}")         #double quote outside, single quote inside

    if (account['limit'] >= amount):
        account['limit'] -= amount
        print("You can take your money")
        checkLimit(account)

    else:
        total = account['limit'] + account['secondLimit']

        if (total >= amount):
            secondAccountUsage = input('Second usage ? (Y/N)')

            if secondAccountUsage == 'Y' or 'y' :
                secondAccountUsageAmount = amount - account['limit']
                account['limit'] = 0
                account['secondLimit'] -= secondAccountUsageAmount 
                print("Take your money")
                checkLimit(account)
            else:
                print(f"{account['accountNumber']} numbered account had {account['limit']} for usage")
        else:
            print("Sadly your limit isn't enough")
            checkLimit(account)

def checkLimit(account):
    print(f"{account['accountNumber']} nolu hesabınızda {account['limit']} TL bulunmaktadır. Your second account limit is {account['secondLimit']}")




moneyDraw(SBAccount, 8500)                     #Input for check
checkLimit(SBAccount)
print('***************************')
moneyDraw(SBAccount, 2150)
checkLimit(SBAccount)
