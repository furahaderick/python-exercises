# Start
# - init years_left_to_retire, current_age, retirement_age to 0
# - prompt for current_age with "What is your current age? "
# - prompt for retirement_age with "At what age would you like to retire? "
# - years_left_to_retire = retirement_age - current_age
# - display "You have {years_left_to_retire} years left until you can retire"
# - display "It's {current_year}, so you can retire in {current_year + years_left_to_retire}"
# End

from datetime import datetime
import sys

years_left_to_retire = 0
current_age = 0
retirement_age = 0
current_year = 0

current_age = int(input("What is your current age? "))
retirement_age = int(input("At what age would you like to retire? "))

years_left_to_retire = retirement_age - current_age

if years_left_to_retire < 0:
    print("You can already retire now")
    # Exit the program
    sys.exit(0)

print(f"You have {years_left_to_retire} years left until you can retire")

current_year = datetime.now().year

print(
    f"It's {current_year}, so you can retire in {current_year + years_left_to_retire}"
)
