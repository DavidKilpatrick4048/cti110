# David Kilpatrick
# 10/17/2024
# P3HW1_KilpatrickDavid
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
sumGrades = mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6
avg = sumGrades / len(grades)

# determine grade information

print()
print('---------Results---------')
print(f'Lowest grade:  {low}')
print(f'Highest grade: {high}')
print(f'Sum of grades: {sumGrades:.2f}')
print(f'Average:       {avg:.2f}')
print('-------------------------')

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')



