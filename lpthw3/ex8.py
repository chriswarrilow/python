# Variable formatter created with {} to be repplaced with .format()input.
formatter = "{} {} {} {}"
# Prints the formatter variable replacements with the specified text.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# Prints just the empty {} as specified in the formatter variable.
print(formatter.format(formatter, formatter, formatter, formatter))

# Prints the text all in one line i think because of the , at the end of each string.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

print(f"{formatter} {formatter}")
