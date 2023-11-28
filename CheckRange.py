#Alex Flores
#November 7, 2023
#Problem 2 CheckRange
# The code will state whether the number chosen is the given range.
Range = range(1, 10)
number = int(input('Please enter a number :'))

if number in Range:
    print(number, 'is in the given range.')
else:
    print(number, 'is not in the given range.')