two_digit_number = input("Type a two digit number: ")
# by default input() returns user input as string
print(type(two_digit_number))
print("\n")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
sum_of_digits = int(first_digit) + int(second_digit)
print(first_digit + " + " + second_digit + " = " + str(sum_of_digits))
print(sum_of_digits)
