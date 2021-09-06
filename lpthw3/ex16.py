# To run you need to specify python filename and filename you wish to edit.
from sys import argv

script, filename = argv
# -------------------------------------------------------------------------
print(f"We're going to erase {filename}.")
print("If you dont want that , hit CTRL-C (^C).")
print("If you do want that hit return.")
# Waits for user input.
input("?")
# Opens specified file.
print("Opening the file...")
target = open(filename, 'w')
# Erases all content inside of specified file.
print("Truncating the file.   Goodbye!")
target.truncate()
# Asking user for text to write to the file, in this case 3 lines.
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
# Writes the 3 lines to the file each on a new line with \n.
print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
# Closes file.
print("And finally, we close it.")
target.close()
