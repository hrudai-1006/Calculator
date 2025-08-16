class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def sub(a, b):
        return a - b
    @staticmethod
    def mul(a, b):
        return a * b
    @staticmethod
    def div(a, b):
        return a / b if b != 0 else "Error: Division by zero"
    @staticmethod
    def mod(a, b):
        return a % b if b != 0 else "Error: Modulo by zero"
    @staticmethod
    def square(a):
        return a ** 2
    @staticmethod
    def sqrt(a):
        return a ** 0.5 if a >= 0 else "Error: Negative Square root"

def get_two_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None, None


while True:
    print("1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVISION\n5.MODULUS(REMAINDER)\n6.SQUARE\n7.SQUARE ROOT\n8.EXIT")
    choice = input()
    if choice == "1":
        print("ENTER THE NUMBERS TO ADD :")
        num1, num2 = get_two_numbers()
        result = Calculator.add(num1, num2)
        print("Result =",result)
    elif choice == "2":
        print("ENTER THE NUMBERS TO SUBTRACT :")
        num1, num2 = get_two_numbers()
        result = Calculator.sub(num1, num2)
        print("Result =",result)
    elif choice == "3":
        print("ENTER THE NUMBERS TO MULTIPLY :")
        num1, num2 = get_two_numbers()
        result = Calculator.mul(num1, num2)
        print("Result =",result)
    elif choice == "4":
        print("ENTER THE NUMBERS TO DIVIDE :")
        num1 , num2 = get_two_numbers()
        result = Calculator.div(num1, num2)
        print("Result =",result)
    elif choice == "5":
        print("ENTER THE NUMBERS TO MODULUS (REMAINDER) :")
        num1, num2 = get_two_numbers()
        result = Calculator.mod(num1, num2)
        print("Result =",result)
    elif choice == "6":
        print("ENTER THE NUMBER TO SQUARE :")
        try:
            a = float(input("Enter a number: "))
            print("Result =", Calculator.square(a))
        except ValueError:
            print("Invalid input!")
    elif choice == "7":
        try:
            a = float(input("Enter a number: "))
            print("Result =", Calculator.sqrt(a))
        except ValueError:
            print("Invalid input!")
    elif choice == "8":
        print("Exiting...")
        print("Goodbye!")
        break
    else:
        print("Invalid input!")
        print("Enter a valid number!")
