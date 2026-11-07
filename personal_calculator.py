name = input("Enter your name: ")

age = input("Enter your age: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2

if num2 != 0:
    div_result = f"{num1 / num2:.1f}"
else:
    div_result = "Undefined (division by zero)"

print(f"\nHello, {name}!")
print(f"Your age is {age}.\n")

print(f"Addition: {sum_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")