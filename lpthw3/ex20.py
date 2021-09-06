from sys import argv

script, input_file = argv
# Creates a function called print_all and assigns a variable (f) to it
def print_all(f):
    print(f.read())
# seek reads bytes so 0 is the begining of a file.
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Lets print three lines:")
# current_line numbers each line at the begining of the output.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
