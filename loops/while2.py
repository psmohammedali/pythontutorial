print("Hacker Rank Question")

# Objective
# In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.
# Task
# Given an integer,
# , print its first multiples. Each multiple (where
#
# ) should be printed on a new line in the form: n x i = result.
#
# Input Format
#
# A single integer,
#
# .
#
# Constraints
#
# Output Format
#
# Print
# lines of output; each line (where ) contains the of in the form:
# n x i = result.

n = int(input("Enter any number: "))

i =1
while i <= 10:
    print(str(n) + " x " + str(i) + "= " + str(i * n))
    i = i+1

print("The loop ended")