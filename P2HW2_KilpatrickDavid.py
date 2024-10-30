# David Kilpatrick
# 10/7/2024
# P2HW1_KilpatrickDavid
# Grade Statistics Program

# //Variables
# Declare float grade1
# Declare float grade2
# Declare float grade3
# Declare float grade4
# Declare float grade5
# Declare float grade6
# //Input
# Display "Enter grade for Module 1:"
# Input grade1
# Display "Enter grade for Module 2:"
# Input grade2
# Display "Enter grade for Module 3:"
# Input grade3
# Display "Enter grade for Module 4:"
# Input grade4
# Display "Enter grade for Module 5:"
# Input grade5
# Display "Enter grade for Module 6:"
# Input grade6
# //Calculations
# lowest_grade = min
# highest_grade = max
# sum_of_grades = sum
# average_grade = sum_of_grades / len(grades)
# //Output
# Display Results
# Display Lowest Grade
# Display Highest Grade
# Display Sum of Grades
# Display Average

grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

grades = [grade1, grade2, grade3, grade4, grade5, grade6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print("\n-----------Results-----------")
print(f"Lowest Grade:     {lowest_grade:.1f}")
print(f"Highest Grade:    {highest_grade:.1f}")
print(f"Sum of Grades:    {sum_of_grades:.1f}")
print(f"Average:          {average_grade:.2f}")
print("-------------------------------------")

