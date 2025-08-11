# Start
# - init quote to ""
# - init author to ""
# - prompt for quote using "What is the quote? "
# - prompt for author using "Who said it? "
# - Display "{author} says, \"{quote}\"."
# End

quote = ""
author = ""

quote = input("What is the quote? ")
author = input("Who said it? ")

print(author + ' says, "' + quote + '."')
