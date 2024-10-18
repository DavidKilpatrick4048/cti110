# David Kilpatrick
# 10/17/2024
# P3LAB_KilpatrickDavid
# Change Calculator

amount = float(input("Enter the amount of money as a float: "))

cents = int(amount * 100)

dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
   
if cents >= 100: #Dollars
        dollars = cents // 100
        cents = cents % 100
    
if cents >= 25: #Quarters
        quarters = cents // 25
        cents = cents % 25
    
if cents >= 10: #Dimes
        dimes = cents // 10
        cents = cents % 10
    
if cents >= 5: #Nickles
        nickels = cents // 5
        cents = cents % 5
    
pennies = cents #leftover pennies
    
# if-else
if amount == 0:
    print("No change")
else:
    
    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
            
        else:
            print(f"{dollars} Dollars")
            
    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")
            
    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")
            
    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")
            
    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")
