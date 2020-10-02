"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""
# What is U.P.E.R.?
# UNDERSTAND
#     Whats our input? :nums (list of numbers), target (int)
#     return the indecies
#     nums can be arbitrary length

# PLAN
#     how do we return the index and not the value
#     iterate over nums list using range so that we have access to the indecies
#     check if the current number + any of the rest of the numbers == target

# EXECUTE

# REFLECT

def two_sum(nums, target):
    # Your code here

    num1 = 0
    num2 = 0

    for i in range(len(nums)):
        num1 = i
        for y in range(i, len(nums)):
            num2 = y
            if nums[i] + nums[y] == target:
                return [num1, num2]

print(two_sum([3, 8, 12, 17], 15))