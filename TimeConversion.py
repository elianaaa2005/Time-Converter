#TIME CALCULATOR
import time
import os
from decimal import Decimal, getcontext
#modules

getcontext().prec = 7

loopCode = True
while loopCode == True:
#while loop, this ensures that the code repeats over and over infinitely

    sValue = 0
    mValue = 0
    hValue = 0
    dValue = 0
    
    print("Convert units of time to other units!")
    print("")
#title
    
    print("Select your initial unit of measurement:")
    print('''1: Seconds
2: Minutes
3: Hours
4: Days''')
    userSelection = int(input())
#selection screen
    
    if userSelection == 1:
        print("Choose the amount of seconds you wish to convert:")
        sValue = int(input())
        mValue = Decimal(sValue) / Decimal(60)
        hValue = Decimal(sValue) / Decimal(3600)
        dValue = Decimal(sValue) / Decimal(86400)
        
        outputResult = '''{} seconds is equal to:
{} minutes
{} hours
{} days'''
        print(outputResult.format(sValue, mValue, hValue, dValue))
        print("")
        
    elif userSelection == 2:
        print("Choose the amount of minutes you wish to convert:")
        mValue = int(input())
        sValue = Decimal(mValue) / Decimal(1/60)
        hValue = Decimal(mValue) / Decimal(60)
        dValue = Decimal(mValue) / Decimal(1440)
        
        outputResult = '''{} minutes is equal to:
{} seconds
{} hours
{} days'''
        print(outputResult.format(mValue, sValue, hValue, dValue))
        print("")
        
    elif userSelection == 3:
        print("Choose the amount of hours you wish to convert:")
        hValue = int(input())
        sValue = Decimal(hValue) / Decimal(1/3600)
        mValue = Decimal(hValue) / Decimal(1/60)
        dValue = Decimal(hValue) / Decimal(24)
        
        outputResult = '''{} hours is equal to:
{} seconds
{} minutes
{} days'''
        print(outputResult.format(hValue, sValue, mValue, dValue))
        print("")
        
    elif userSelection == 4:
        print("Choose the amount of days you wish to convert:")
        dValue = int(input())
        sValue = Decimal(dValue) / Decimal(1/86400)
        mValue = Decimal(dValue) / Decimal(1/1440)
        hValue = Decimal(dValue) / Decimal(1/24)
        
        outputResult = '''{} days is equal to:
{} seconds
{} minutes
{} hours'''
        print(outputResult.format(dValue, sValue, mValue, hValue))
        print("")
        
    else:
        print("Invalid input, please enter a valid number from 1 to 4.")
    time.sleep(2)
    input("Press enter to continue:")
    print("")
    os.system('cls')
#end of code
