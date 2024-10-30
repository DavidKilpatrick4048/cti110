# David Kilpatrick
# 10/01/2024
# P2LAB2
# Car Dictionary MPG Calculator

vehicles = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = vehicles.keys()

print(keys)

vehicle = input("Enter a vehicle to see it's mpg: ")
print()
mpg = vehicles[vehicle]
print(f"The {vehicle} gets {mpg} mpg.")
print()
miles = float(input(f"How many miles will you drive the {vehicle}?"))
print()
gas = miles / mpg
print(f"{gas:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")

