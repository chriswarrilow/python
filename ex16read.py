from sys import argv

script, filename = argv

txt = open(filename)
print(f"Here is the content of {filename}: ")
print(txt.read())

txt.close()
