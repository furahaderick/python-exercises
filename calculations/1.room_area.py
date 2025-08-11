# Start
# - init length, width, normal_area, converted_area, unit_choice to 0
# - init unit_used, unit_not_used to ""
# - prompt for unit_choice using "Which units do you want to use? "
# - determine unit_used from unit_choice
# - prompt for length using "What is the length of the room in {unit_used}? "
# - prompt for width using "What is the width of the room in {unit_used}? "
# - display "You entered dimensions of {length} {unit_used} by {width} {unit_used}"
# - normal_area = length * width
# - converted_area = check if feet units are used
#       If yes: converted_area = normal_area * 0.09290304
#       If no: converted_area = normal_area / 0.09290304
# - display "{normal_area} square {unit_used}"
# - display "{converted_area} square {other_unit}"
# End

from enum import Enum

length = 0
width = 0
normal_area = 0
converted_area = 0

unit_choice = 0
unit_used = ""
unit_not_used = ""


def get_unit_chosen(choice):
    return "feet" if choice == 1 else "meters"


def get_unit_not_chosen(choice):
    return "feet" if choice != 1 else "meters"


class Constants(Enum):
    CONVERSION_FACTOR = 0.09290304


try:

    unit_choice = int(
        input(
            "Which units do you want to use? (Choose number):\n1. Feet\n2. Meters\nYour choice: "
        )
    )

    if unit_choice not in [1, 2]:
        raise ValueError

    unit_used = get_unit_chosen(unit_choice)

    unit_not_used = get_unit_not_chosen(unit_choice)

    length = abs(float(input(f"What is the length of the room in {unit_used}? ")))
    width = abs(float(input(f"What is the width of the room in {unit_used}? ")))

    print(f"You entered dimensions of {length} {unit_used} by {width} {unit_used}")

    normal_area = length * width

    converted_area = (
        round(normal_area * Constants.CONVERSION_FACTOR.value, 3)
        if unit_choice == 1
        else round(normal_area / Constants.CONVERSION_FACTOR.value, 3)
    )

    print(f"{normal_area} square {unit_used}\n{converted_area} square {unit_not_used}")

except ValueError:
    print("Invalid input received")
