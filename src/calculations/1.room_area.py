# Start
# - init length, width, area_in_ft, area_in_sqm to 0
# - prompt for length using "What is the length of the room in ft? "
# - prompt for width using "What is the width of the room in ft? "
# - display "You entered dimensions of {length} feet by {width} feet"
# - area_in_ft = length * width
# - area_in_sqm = (area_in_ft ** 2) * 0.09290304 (Rounded upto 3 decimal places)
# - display "{area_in_ft} square feet"
# - display "{area_in_sqm} square meters"
# End

from enum import Enum

length = 0
width = 0
area_in_ft = 0
area_in_sqm = 0


class Constants(Enum):
    CONVERSION_FACTOR = 0.09290304


try:
    length = float(input("What is the length of the room in ft? "))
    width = float(input("What is the width of the room in ft? "))

    print(f"You entered dimensions of {length} feet by {width} feet")

    area_in_ft = length * width
    area_in_sqm = round(area_in_ft * Constants.CONVERSION_FACTOR.value, 3)

    print(f"{area_in_ft} square feet\n{area_in_sqm} square meters")

except ValueError:
    print("Invalid input received")
