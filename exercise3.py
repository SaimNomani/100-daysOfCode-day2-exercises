# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until
# 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x days, y weeks, and z months left.
#
# Where x, y and z are replaced with the actual calculated numbers.
#
# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.
#
# Hint
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
#
age = input("What is your current age? ")
age = 90 - int(age)
print(f"You have {age * 365} days, {age * 52} weeks, and {age * 12} months left.")
