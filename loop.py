# loop
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# nested loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# range automatically increases the value of the x by iterating 

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# while loop 
number = 100
while number > 0:
    print(number)
    number //= 2 # floor division (removes the decimal part) 100, 50, 25, 12, 6, 3, 1


command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

count = 0
for number in range(2, 10, 2):
    print(number)
    count += 1

print(f"We have {count} even numbers")

# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers")
