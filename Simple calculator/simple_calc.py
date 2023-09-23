# Function to perform addition
def add(x, y):
    result = x + y
    return result, "Sum of {} and {} is {}".format(x, y, result)

# Function to perform subtraction
def subtract(x, y):
    result = x - y
    return result, "{} minus {} equals {}".format(x, y, result)

# Function to perform multiplication
def multiply(x, y):
    result = x * y
    return result, "{} multiplied by {} is {}".format(x, y, result)

# Function to perform division
def divide(x, y):
    if y == 0:
        return None, "Cannot divide by zero"
    result = x / y
    return result, "{} divided by {} is {}".format(x, y, result)

# Main calculator loop
while True:
    # Display menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")

    # User input
    user_input = input("- ")

    if user_input == "exit":
        break

    if user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            result, description = add(num1, num2)
        elif user_input == "subtract":
            result, description = subtract(num1, num2)
        elif user_input == "multiply":
            result, description = multiply(num1, num2)
        elif user_input == "divide":
            result, description = divide(num1, num2)

        if result is not None:
            print(description)
        else:
            print(description)
    else:
        print("Invalid input")
