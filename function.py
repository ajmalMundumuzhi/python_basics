def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("John", "Doe")

# def multiply(x, y):
#     return x * y

# result = multiply(3, 4)
# print(result)  # Output: 12

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number # total = total * number
    return total

print(multiply(2,3,4,5))