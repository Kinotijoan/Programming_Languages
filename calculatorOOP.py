# JOAN NKATHA KINOTI
# SCT 211-0042/2022

class Calculator:
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def Sum(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def divide(self):
        try:
          return self.num1 / self.num2
        except ZeroDivisionError:
            print("Cannot divide by zero")

    def multiply(self):
        return self.num1 * self.num2

    def getInput(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))
        self.operation = str(input("What operation do you want to perform on the numbers? "))

    def eval(self):
        if self.operation == "+":
            return self.Sum()
        elif self.operation == "-":
            return self.subtract()
        elif self.operation == "*":
            return self.multiply()
        elif self.operation == "/":
            return self.divide()
        else:
            print("Invalid operation")
            self.operation = input("What operation do you want to perform on the numbers? ")


def main():
    calc = Calculator(num1=None,num2=None,operation=None)
    calc.getInput()
    result = calc.eval()
    print("Result:", result)


if __name__ == "__main__":
    main()