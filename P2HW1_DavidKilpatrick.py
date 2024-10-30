# David Kilpatrick
# 10/7/2024
# P2HW1_
# Pretty Math Program - Travel Expenses

# //Variables
# Declare float budget
# Declare string destination
# Declare float gas
# Declare float accomodation
# Declare float food
# //Input
# Display "Enter Budget"
# Input budget
# Display "Enter your travel destination:
# Input destination
# Display "How much do you think you will spend on gas"
# Input gas
# Display "Approximately, how much will you need for accomodation/hotel"
# Input accomodation
# Display "Last, how much do you need for food"
# Input food
# //Calculations
# Set remaining = budget - (gas + accomodation + food)
# //Output
# Display "Remaining Balance" remaining


print("This program calculates and displays travel expenses")
print() # blank line
print('Enter Budget: ', end='')
budget = float(input()) # Declare integer budget
print() # blank line
print('Enter your travel Destination: ', end='') 
destination = input() # Declare string Destination
print() # blank line
print('How much do you think you will spend on gas? ', end='')
gas = float(input()) #delare integer gas
print() # blank line
print('Approximately, how much will you need for accomodation/hotel? ', end='')
accomodation = float(input()) #declare integer accomodation
print() # blank line
print('Last, how much do you need for food? ', end='')
food = float(input()) #declare integer food
print() # blank line
print("------------Travel Expenses------------")
print(f"Location:          {destination}")
print(f"Initial Budget:    ${budget:.2f}")
print(f"Fuel:              ${gas:.2f}")
print(f"Accomodation:      ${accomodation:.2f}")
print(f"Food:              ${food:.2f}")
print("---------------------------------------")
remaining = budget - (gas + accomodation + food)
print() # blank line
print(f"Remaining Balance: ${remaining:.2f}")

