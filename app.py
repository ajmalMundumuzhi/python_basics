course = "Python Programming 101"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:6])
print(course[0:], "ds")
print(course[:6])
print(course.lower())

# \"
# \'
# \\
# \n
class_name = 'Python \'Programming'
print(class_name)

first = "Mohammed"
last = "Ajmal"
full = f"{first} {last}"
full_length = f"{len(first)} {len(last)}"
print(full)
print(full_length)

module = "pythoN programming"

print(module.upper())
print(module.lower())
print(module.title())
print(module.strip()) # l for removing whitespace at the beginning and r for end of the string
print(module.replace("N", "n"))
print(module.find("Pro")) # output will be -1 (it means not found)
print("pro" in module)
print("swift" not in module)

x = 10
x = x + 3
x += 3 # x = x + 3 (shorthand)
print(x)

import math

print(round(2.9))
print(abs(-2.9)) # check how much distance to zero

print(math.ceil(2.2)) # checks which is the next integer and returns it