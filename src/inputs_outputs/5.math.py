# Start
# - init num1, num2, total, difference, product, quotient to 0
# - prompt for the numbers using "What is the 1st/2nd number? "
# - compute the arithmetic operations
# - display results
# End

num1 = 0
num2 = 0
total = 0
difference = 0
product = 0
quotient = 0


def computeSum(a, b):
    return round(a + b, 2)


def computeDifference(a, b):
    return round(a - b, 2)


def computeProduct(a, b):
    return round(a * b, 2)


def computeQuotient(a, b):
    return round(a / b, 2)


num1 = input("What is the 1st number? ")
num2 = input("What is the 2nd number? ")

try:
    num1 = float(num1)
    num2 = float(num2)

    # Check if numbers are negative
    if num1 < 0 or num2 < 0:
        raise ValueError

    total = computeSum(num1, num2)
    difference = computeDifference(num1, num2)
    product = computeProduct(num1, num2)
    quotient = computeQuotient(num1, num2)

    print(
        f"{num1} + {num2} = {total}\n{num1} - {num2} = {difference}\n{num1} x {num2} = {product}\n{num1} / {num2} = {quotient}"
    )
except ValueError:
    print("Only positive, valid numbers are allowed")
