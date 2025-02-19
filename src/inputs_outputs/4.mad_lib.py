# Start
# - init noun, verb, adverb, adjective to ""
# - prompt for each part of speech using "Enter a/an {part_of_speech}: "
# - display story containing those parts of speech
# End

noun = ""
verb = ""
adverb = ""
adjective = ""

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
adjective = input("Enter an adjective: ")

print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")


# Another algorithm below - it works!

# value_iterator = {"noun": "", "verb": "", "adverb": "", "adjective": ""}

# for part_of_speech in list(value_iterator.keys()):
#     value = input(f"Enter a/an {part_of_speech}: ")
#     value_iterator[f"{part_of_speech}"] = value

# print(
#     f"Do you {value_iterator.get('verb')} your {value_iterator.get('adjective')} {value_iterator.get('noun')} {value_iterator.get('adverb')}? That's hilarious!"
# )
