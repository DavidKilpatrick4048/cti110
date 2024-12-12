# David Kilpatrick
# 11/8/2024
# P4HW2_KilpatrickDavid
# Payroll/Overtime Calculator

#Pseudocode
# //Variables
# Declare total_employees, total_overtime_pay, total_regular_pay, total_gross_pay, overtime_hours, regular_hours, hours, pay_rate, name
#//Inputs
# Display "Enter number of hours worked", hours
# Display "Enter employee's pay rate", pay_rate
# If hours > 40
#   set overtime_hours = hours - 40
#   set regular_hours = 40
# else
#   set overtime_hours = 0
#   Set regular_hours = hours
# //Calculations
# regular_pay = regular_hours * pay_rate
# overtime_pay = overtime_hours * (payrate * 1.5)
# gross_pay = regular_pay + overtime_pay
#//Outputs
# display ----------------------------------------
# display "Employee Name:", name
# display blank line
# display "Hours Worked    Pay Rate       OverTime         OverTime Pay     RegHour Pay       Gross Pay"
# display hours, pay_rate, overtime_hours, overtime_pay, regular_pay, gross_pay"
# IF total_employees > 0
#   print total_employees
#   print total_overtime_pay
#   print total_regular_pay
#   print total_gross_pay
# Else "no information was entered"

total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    name = input("Enter employee's name or Done to Terminate: ")
    if name == 'Done':
        break
    hours = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    
    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    total_employees += 1    
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    print("----------------------------------------")
    print(f"Employee name:  {name}")
    print()
    print("Hours Worked    Pay Rate       OverTime         OverTime Pay     RegHour Pay       Gross Pay")
    print("-----------------------------------------------------------------------------------------------")
    print(f"{hours:<16.1f}{pay_rate:<15.1f}{overtime_hours:<17.1f}{overtime_pay:<17.2f}${regular_pay:<17.2f}${gross_pay:<17.2f}")
if total_employees > 0:
    print("\n")
    print(f"Total number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay}")
    print(f"Total amount paid for regular hours: ${total_regular_pay}")
    print(f"Total amount paid in gross: ${total_gross_pay}")
else:
    print("No information was entered.")


