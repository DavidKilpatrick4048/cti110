# David Kilpatrick
# 11/13/2024
# P5LAB_KilpatrickDavid
# SelfCheckout Practice Machine

import random

def disperse_change(amount):
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

def main():
    purchase_amount = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${purchase_amount:.2f}")

    while True:
            payment = float(input("How much cash will you put in the self-checkout? "))

            if payment < purchase_amount:
                print("Insufficient Payment")
                continue
            else:
                change = round(payment - purchase_amount, 2)
                print(f"Your change is: ${change:.2f}")
                disperse_change(change)

main()
