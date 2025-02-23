# Start
# - init num_of_people, num_of_pizzas, num_of_slices, slices_per_person, leftover_count to 0
# - prompt for num_of_people using "How many people? "
# - prompt for num_of_pizzas using "How many pizzas? "
# - prompt for num_of_slices using "How many slices per pizza? " (Should be even)
# - slices_per_person = (num_of_slices * num_of_pizzas) / num_of_people (Floor division)
# - leftover_count = (num_of_slices * num_of_pizzas) % num_of_people
# - display "{num_of_people} with {num_of_pizzas} pizzas, {num_of_slices} slices each..."
# - display "Each person gets {slices_per_person} pieces of pizza."
# - display "There are {leftover_count} leftover pieces."
# End

import sys

num_of_ppl = 0
num_of_pizzas = 0
num_of_slices = 0
slices_per_person = 0
leftover_count = 0

try:
    num_of_ppl = int(input("How many people? "))
    num_of_pizzas = int(input("How many pizzas? "))
    num_of_slices = int(input("How many slices per pizza? "))
except ValueError:
    print("error: Invalid input received")
    sys.exit(1)

if num_of_slices % 2 != 0:
    print("error: The number of slices should be even")
    sys.exit(1)

slices_per_person = (num_of_slices * num_of_pizzas) // num_of_ppl
leftover_count = (num_of_slices * num_of_pizzas) % num_of_ppl

print(f"{num_of_ppl} with {num_of_pizzas} pizzas, {num_of_slices} slices each...")
print(
    f"Each person gets {slices_per_person} piece{'s' if slices_per_person > 1 else ''} each."
)

if leftover_count == 0:
    print("There are no leftover pieces of pizza")
else:
    print(
        f"There {'are' if leftover_count > 1 else 'is'} {leftover_count} leftover piece{'s' if leftover_count > 1 else ''}."
    )
