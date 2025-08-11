# Start
# init fahrenheit_qty, celcius_qty, input, output to 0
# init choice to ""
# display starting guidelines and Prompt for choice
# IF choice == "C":
#   prompt for numberical input
#   fahrenheit_qty = input
#   celcius_qty = computeCelciusQty(fahnreinheit_qty)
#   output = celcius_qty
#   display "The temp in Celcius is {output}"
# ELSE:
#   prompt for numberical input
#   celcius_qty = input
#   fahrenheit_qty = computeFahrenheitQty(celcius_qty)
#   output = fahrenheit_qty
#   display "The temp in Fahrenheit is {output}"
# End

fahrenheit_qty = 0
celcius_qty = 0
input_val = 0
output_val = 0
choice = ""


class InvalidChoiceException(Exception):
    pass


def computeCelciusQty(f):
    c = (f - 32) * (5 / 9)
    return c


def computeFahrenheitQty(c):
    f = (c * (9 / 5)) + 32
    return f


print("Press C to convert from Fahrenheit to Celcius.")
print("Press F to convert from Celcius to Fahrenheit.")

try:
    choice = input("Your choice: ").capitalize()

    if choice not in ["C", "F"]:
        raise InvalidChoiceException()

    if choice == "C":
        input_val = float(input("Please enter the temperature in Fahrenheit: "))
        fahrenheit_qty = input_val
        celcius_qty = computeCelciusQty(fahrenheit_qty)
        output_val = round(celcius_qty, 2)
    else:
        input_val = float(input("Please enter the temperature in Celcius: "))
        celcius_qty = input_val
        fahrenheit_qty = computeFahrenheitQty(celcius_qty)
        output_val = round(fahrenheit_qty, 2)
except ValueError:
    print("Invalid numerals received")
except InvalidChoiceException:
    print("Wrong conversion choice")
else:
    print(
        f"The temperature in {'Celcius' if choice == 'C' else 'Fahrenheit'} is {output_val}"
    )
