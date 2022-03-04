def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


choice = int(input("""please choose one operation:
1 - add
2 - subtract
3 - multiply
4 - divide
"""))

num1 = int(input("Input your first number: "))
num2 = int(input("Input your second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid Option")
