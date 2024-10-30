# David Kilpatrick
# 10/29/2024
# P4LAB2
# Calculation Table Display

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        for multiple in range(1,13):
            print(f"{user_num} * {multiple} = {user_num * multiple}")
    else:
        print("This program does not handle negative numbers")

    run_again = input("Would you like to run the program again?")        

print("Program is ending....")    
