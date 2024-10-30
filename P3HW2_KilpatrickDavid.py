# David Kilpatrick
# 10/24/2024
# P3HW2_KilpatrickDavid
# Payroll/Overtime Calculator

#Pseudocode
# //Variables
# Declare float hours, pay_rate
# //If Statement
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


name = input("Enter employee's name: ")
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
    

print("----------------------------------------")
print(f"Employee name:  {name}")
print()
print("Hours Worked    Pay Rate       OverTime         OverTime Pay     RegHour Pay       Gross Pay")
print("-----------------------------------------------------------------------------------------------")
print(f"{hours:<16.1f}{pay_rate:<15.1f}{overtime_hours:<17.1f}{overtime_pay:<17.2f}${regular_pay:<17.2f}${gross_pay:<17.2f}")


