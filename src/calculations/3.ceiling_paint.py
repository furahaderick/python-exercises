# Start
# - init gallons_required, length, width, area to 0
# - prompt for the length using "What is the length of the room? (ft) "
# - prompt for the width using "What is the width of the room? (ft) "
# - area = length * width
# - gallons_required = math.ceil(area / 350)
# - display "You will need to purchase {gallons_required} gallons of paint to cover {area} square feet."
# End

from enum import Enum
import math
import sys

gallons_required = 0
length = 0
width = 0
area = 0


class Constants(Enum):
    AREA_COVERED_BY_A_GALLON = 350


length = float(input("What is the length of the room? (ft): "))
width = float(input("What is the width of the room? (ft): "))

if width > length:
    print("The width cannot be longer than the length.")
    sys.exit(0)

area = length * width

gallons_required = math.ceil(area / Constants.AREA_COVERED_BY_A_GALLON.value)

print(
    f"You will need to purchase {gallons_required} gallons of paint to cover {area} square feet."
)
