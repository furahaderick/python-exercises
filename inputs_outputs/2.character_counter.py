# Start
# - init input_string to ""
# - init char_count to 0
# - prompt for input_string using "What is the input string? "
# - count the characters in input_string (Python uses the len() function)
# - Display "{input_string} has {char_count} characters."
# End

input_string = ""
char_count = 0

input_string = input("What is the input string? ")

char_count = len(input_string)

if char_count == 0:
    print("You cannot enter an empty string.")
else:
    print(f"{input_string} has {char_count} characters.")
