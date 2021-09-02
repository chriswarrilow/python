from sys import argv
# read the WYSS section for how to run this
script, first, second, third, forth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", forth)

fifth = input("What is your fifth variable? ")
print(f"{fifth}")

print("What about your sixth variable? ")
sixth = input()
