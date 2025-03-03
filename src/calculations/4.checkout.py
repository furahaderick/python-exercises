# Start
# - init price_1, count_1 ... 3, sub_total, total, tax to 0
# - sub_total = (price_1 * count_1 ... 3)
# - tax = sub_total * 0.055
# - total = sub_total + tax
# End

from enum import Enum

price_1 = 0
count_1 = 0

price_2 = 0
count_2 = 0

price_3 = 0
count_3 = 0

sub_total = 0
total = 0
tax = 0


class Constants(Enum):
    TAX_RATE = 0.055


try:
    price_1 = float(input("Enter the price of item 1: "))
    count_1 = float(input("Enter the quantity of item 1: "))

    price_2 = float(input("Enter the price of item 2: "))
    count_2 = float(input("Enter the quantity of item 2: "))

    price_3 = float(input("Enter the price of item 3: "))
    count_3 = float(input("Enter the quantity of item 3: "))

    if (
        (price_1 <= 0 and count_1 > 0)
        or (price_2 <= 0 and count_2 > 0)
        or (price_3 <= 0 and count_3 > 0)
    ) or (count_1 < 0 or count_2 < 0 or count_3 < 0):
        raise Exception("Your counting doesn't make sense")

except ValueError:
    print("Please enter valid numbers")
except Exception as error:
    print(f"Error: {error}")
else:
    sub_total = (price_1 * count_1) + (price_2 * count_2) + (price_3 * count_3)
    tax = sub_total * Constants.TAX_RATE.value
    total = sub_total + tax

    print(f"Subtotal: ${sub_total}\nTax: ${tax}\nTotal: ${total}")
finally:
    pass
