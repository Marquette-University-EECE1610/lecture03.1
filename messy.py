# This program works, but it is hard to read, hard to change,
# and repeats logic. Your job is to refactor it into functions.

print("Calculate overall score for first student:")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
homework = float(input("Enter homework average: "))
project = float(input("Enter project score: "))

score = exam1 * 0.25 + exam2 * 0.25 + homework * 0.20 + project * 0.30
print("Overall score:", score)

print("Calculate overall score for second student:")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
homework = float(input("Enter homework average: "))
project = float(input("Enter project score: "))

# weights (magic numbers scattered everywhere)
score = exam1 * 0.25 + exam2 * 0.25 + homework * 0.20 + project * 0.30
print("Overall score:", score)

print("Calculate overall score for third student:")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
homework = float(input("Enter homework average: "))
project = float(input("Enter project score: "))

# weights (magic numbers scattered everywhere)
score = exam1 * 0.25 + exam2 * 0.25 + homework * 0.20 + project * 0.30
print("Overall score:", score)
