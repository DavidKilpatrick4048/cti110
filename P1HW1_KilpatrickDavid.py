 # David Kilpatrick
 # 09/18/2024
 # P1HW1
 # Program to do some math

print("-----Calculating Exponents-----\n")

base = int(input("Enter an integer as the base value: "))
exponent =int(input("Enter an integer as the exponent: "))
print() #blank line
result = base ** exponent 
print(base, 'raised to the power of' , exponent, 'is', result, "!!\n")

print("-----Addition and Subtraction-----\n")
base1 = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter and integer to subtract: "))
print() #blank line
final = base1 + add - subtract
print(base1, '+', add, '-', subtract, "is equal to", final)
