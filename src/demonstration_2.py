"""
Given an integer value `n`, write a function that will return a list of the string representation of numbers from 1 to `n`.

However, there are a few additional rules to follow:

- For multiples of three, it should output "Lambda" instead of the number.
- For multiples of five, it should output "School" instead of the number.
- For numbers which are multiples of three and five, it should output "LambdaSchool" instead of the number.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Lambda",
    "4",
    "School",
    "Lambda",
    "7",
    "8",
    "Lambda",
    "School",
    "11",
    "Lambda",
    "13",
    "14",
    "LambdaSchool"
]
"""
# UNDERSTAND
#     Creates list of numbers
#     Multiples of 3 are replaced with Lambda
#     Multiples of 5 are replaced with School
#     Multiples of 15 are replaced with LambdaSchool

# PLAN
#     While loop to add the number as a string to the list
#     Check for Multiples and add the appropriate string

# EXECUTE

# REFLECT
def lambda_school(n):
    # Your code here
    newList = []
    firstWord = "Lambda"
    secondWord = "School"

    i = 0
    while i < n:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            newList.append(firstWord + secondWord)
        elif i % 3 == 0:
            newList.append(firstWord)
        elif i % 5 == 0:
            newList.append(secondWord)
        else:
            newList.append(str(i))

    return newList


print(lambda_school(15))
