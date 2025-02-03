def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
# print(operations['*'](4,8))

first_number = float(input("What's the first number?: "))
for key in operations:
    print(key)
operation = input("Pick an operation: ")
second_number = float(input("What's the next number?: "))
current_result = operations[operation](first_number, second_number)
print(f"{first_number} {operation} {second_number} = {current_result}")

will_continue = input(
    f"Type 'y' to continue calculating with {current_result}, or type 'n' to start a new calculation: "
).lower()

for key in operations:
    print(key)
operation = input("Pick an operation: ")

if will_continue == 'y':
    for key in operations:
        print(key)
    operation = input("Pick an operation: ")