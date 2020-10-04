"""
Given a `string`, write a function that finds the first non-repeating character in the `string` and return its index. If it doesn't exist, return -1.

Examples:

string = "lambdaschool"
return 2.

string = "lovelambdaschool"
return 2.

string = "abcabc"
return -1.
"""
# UNDERSTAND
#     Check for non repeating characters.
#     If none are found return a -1
#     If a unique character is found return its index

# PLAN
#

# EXECUTE

# REFLECT
def first_unique_char(string):
    # Your code here
    newList = [char for char in string]
    num = 0

    for i in range(len(string)):
        # print(string.count(newList[i]))
        if string.count(newList[i]) > 1:
            num = -1
        elif string.count(newList[i]) == 1:
            return i

    return num

print(first_unique_char("lambdaschool"))
print(first_unique_char("lovelambdaschool"))
print(first_unique_char("abcabc"))
