# Start
# - init price_1, count_1 ... 3, sub_total, total, tax to 0
# - sub_total = (price_1 * count_1 ... 3)
# - tax = sub_total * 0.055
# - total = sub_total + tax
# End

# from enum import Enum

# price_1 = 0
# count_1 = 0

# price_2 = 0
# count_2 = 0

# price_3 = 0
# count_3 = 0

# sub_total = 0
# total = 0
# tax = 0


# class Constants(Enum):
#     TAX_RATE = 0.055


# try:
#     price_1 = float(input("Enter the price of item 1: "))
#     count_1 = float(input("Enter the quantity of item 1: "))

#     price_2 = float(input("Enter the price of item 2: "))
#     count_2 = float(input("Enter the quantity of item 2: "))

#     price_3 = float(input("Enter the price of item 3: "))
#     count_3 = float(input("Enter the quantity of item 3: "))

#     if (
#         (price_1 <= 0 and count_1 > 0)
#         or (price_2 <= 0 and count_2 > 0)
#         or (price_3 <= 0 and count_3 > 0)
#     ) or (count_1 < 0 or count_2 < 0 or count_3 < 0):
#         raise Exception("Your counting doesn't make sense")

# except ValueError:
#     print("Please enter valid numbers")
# except Exception as error:
#     print(f"Error: {error}")
# else:
#     sub_total = (price_1 * count_1) + (price_2 * count_2) + (price_3 * count_3)
#     tax = sub_total * Constants.TAX_RATE.value
#     total = sub_total + tax

#     print(f"Subtotal: ${sub_total}\nTax: ${tax}\nTotal: ${total}")
# finally:
#     pass

# Endless program (until the users wishes so!)

# Start
# - init prices_list, count_list to []
# - init sub_total, tax, total to 0
# - init loop = True
# - while loop == True:
#     - prompt for price n with "Enter the price of the items: "
#     - prompt for quantity n with "Enter the quantity of the items: "
#     - prices_list.append(price n)
#     - count_list.append(quantity n)
#     - prompt if the user wants to add another entry  with "..."
#         - If no
#             - loop = False
# - sub_total = (price_1 * count_1 ... n)
# - tax = sub_total * 0.055
# - total = sub_total + tax
# End

import sys
from enum import Enum


class Constants(Enum):
    TAX_RATE = 0.055


prices_list = []
count_list = []

sub_total = 0
tax = 0
total = 0

loop = True


class InvalidContinuationChoiceException(Exception):
    pass


class CrazyCountingException(Exception):
    pass


while loop == True:
    try:
        price = float(input("Enter the item price: "))
        count = float(input("Enter the quantity of the items: "))

        if (price <= 0 and count > 0) or (count < 0):
            raise CrazyCountingException()

        prices_list.append(price)
        count_list.append(count)

        choice = input("Want to add another entry? (Y/N) ")
        if choice not in ["Y", "N", "y", "n"]:
            raise InvalidContinuationChoiceException()

        if choice in ["N", "n"]:
            loop = False

    except ValueError:
        print("Please enter valid numbers")
        sys.exit(0)
    except CrazyCountingException:
        print("Your counting does not make sense")
        sys.exit(0)
    except InvalidContinuationChoiceException:
        print("Invalid continuation choice")
        break

for index, item in enumerate(count_list):
    sub_total += count_list[index] * prices_list[index]

tax = sub_total * Constants.TAX_RATE.value
total = sub_total + tax

print(f"Subtotal: ${sub_total}\nTax: ${tax}\nTotal: ${total}")
