# replace letters with their corresponding number in alphabetical order
import sys
import re # use of regex for character check in string 
program_name = sys.argv[0] # 1st element in argument values list (script name)
word = sys.argv[1] # 2nd element in argument values list (first parameter)

# these are ansi codes. where \033 is escape character and [31m tells terminal to switch text to red. [0m is a reset 
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
reset = "\033[0m"


print(f'Welcome, you have run {green}{program_name}{reset}. This will give you the letter number in the alphabet')
#check valid letters, otherwise print error and end
if re.fullmatch(r"[A-Za-z]+", word):
    number_word = ''
    # iterate over word string characters to convert each character to a numeric position in the alphabet
    for letter in word:
        number_word += f"{green}{letter}{reset}" + "=" + f"{yellow}{str(ord(letter.upper()) - ord('A') + 1)}{reset}" + " "
        # use of unicode number (referencing ascii table) for letter (uppercase of letter)
        # subtract 66 (A's unicode number + 1) to get position in alphabet (common patten)
    print(number_word)
else:
    print(f"{red}invalid argument given. Please use only A-Z a-z{reset}")

