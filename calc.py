def calculator(a,b,option):
    match option:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b
        case _:
            return "Not A Valid Option"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose an option:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option = int(input("Enter option (1/2/3/4): "))
result = calculator(a,b,option)
print(result)
