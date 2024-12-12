# David Kilpatrick
# 11/8/2024
# P4HW1_KilpatrickDavid
# Grade Average and Letter Grade Program

#Pseudocode
#//Variables
# Declare float num_scores, score
#//Loop statement
#While scores
#   If 0 <= score <=100
#       add 1 to scores
#   else
#       print "INVALID score entered!!!!"
#       print "Score should be between 0 and 100"
#//List
#Determine lowest score entered in scores
#Remove lowest score entered
#Create new list modified_scores
#//Calculation
#Find average of scores
#//If statement
#    if average >= 90
#        set grade to A
#    elif average >= 80
#       set grade to B
#    elif average >= 70
#        set grade to C
#    elif average >= 60
#        set grade to D
#    else
#        set grade to F
#//Outputs
#Lowest Score, lowest_score
#Modified List, modified scores
#Scores Average, average
#Grade, grade

num_scores = int(input("How many scores do you want to enter?"))

scores = []
for i in range(num_scores):
    while True:
        score = input(f"Enter score #{i+1}: ")
        score = float(score)
        if 0 <= score <= 100:
            if len(scores) < i + 1:
                    scores.append(score)
            else:
                    scores[i] = score
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

lowest_score = min(scores)
modified_scores = scores.copy()
modified_scores.remove(lowest_score)

average = sum(modified_scores) / len(modified_scores)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\n" + "---------------" + "Results" + "----------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------------")
