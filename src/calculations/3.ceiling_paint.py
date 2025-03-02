# Start
# - init gallons_required, length, width, radius area, choice to 0
# - Prompt if the room is rounded or rectangular
# - If the room is rectangular:
#   - prompt for the length using "What is the length of the room? (ft) "
#   - prompt for the width using "What is the width of the room? (ft) "
#   - area = length * width
# - If the room is rounded:
#   - prompt for the radius using "What is the radius of the room? (ft) "
#   - area = pi * radius ** 2
# - gallons_required = math.ceil(area / 350)
# - display "You will need to purchase {gallons_required} gallons of paint to cover {area} square feet."
# End

from enum import Enum
import math
import sys

gallons_required = 0
length = 0
width = 0
radius = 0
area = 0
choice = 0


class Constants(Enum):
    AREA_COVERED_BY_A_GALLON = 350
    PI = math.pi


choice = int(
    input(
        "What is the shape of your room?\n1. Rectangular\n2. Rounded\n(Choose number): "
    )
)

if choice not in [1, 2]:
    print("Invalid shape choice.")
    sys.exit(0)

if choice == 1:
    try:
        length = float(input("What is the length of the room? (ft): "))
        width = float(input("What is the width of the room? (ft): "))
        if length <= 0.0 or width <= 0.0:
            raise ValueError

    except ValueError:
        print("Please enter valid, positive numbers.")
        sys.exit(0)

    if width > length:
        print("The width cannot be longer than the length.")
        sys.exit(0)

    area = length * width
else:
    try:
        radius = float(input("What is the radius of the room? (ft): "))
        if radius <= 0:
            raise ValueError
    except ValueError:
        print("Please enter valid, positive numbers.")
        sys.exit(0)

    area = round(Constants.PI.value * radius**2, 3)

gallons_required = math.ceil(area / Constants.AREA_COVERED_BY_A_GALLON.value)

print(
    f"You will need to purchase {gallons_required} gallons of paint to cover {area} square feet."
)
