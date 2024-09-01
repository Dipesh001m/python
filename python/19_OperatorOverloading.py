
"""class Number:
    def __init__(self, num):
        self.num = num
        
        
    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Lets mul")
        return self.num * num2.num
    
n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)"""

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    """Main calculator function"""
    print("Simple Calculator")

    while True:
        # User input for operation choice
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1, 2, 3, 4, 5): ")

        # Check if the choice is to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the choice is valid
        if choice in ('1', '2', '3', '4'):
            # User input for numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the selected operation
            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    calculator()
