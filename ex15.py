# Lines 1 and 2 uses argv to get a filename.
from sys import argv

script, filename = argv
# Creates a variable amd "opens" the filename assigned.
txt = open(filename)
# Prints the output of the users specified file.
print(f"Here's your file {filename}:")
print(txt.read())
# Basically does it all again but with a custom input.
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
