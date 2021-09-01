# Variable for Number of types of people.
types_of_people = 10
# f string printing out how many types of people.
x = f"There are {types_of_people} types of people."
# Variables for weird stuff
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Printing out variables x and y.
print(x)
print(y)
# Printing out variables x and y within an f string.
print(f"I said: {x}")
print(f"I also said: '{y}'")
# Variable set for hilarious and joke_evaluation to print text.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# Printing out the joke_evaluation variable along with the hilarious variable using the .format instead of f strings.
print(joke_evaluation.format(hilarious))
# Variables for w and e to print out.
w = "This is the left side of..."
e = "a string with a right side"
# Printing out variables w and e on one single line using the + .
print (w + e)
