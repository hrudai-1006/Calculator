from flask import Flask, render_template, request

app = Flask(__name__)

class Calculator:
    @staticmethod
    def add(a, b): return a + b
    @staticmethod
    def sub(a, b): return a - b
    @staticmethod
    def mul(a, b): return a * b
    @staticmethod
    def div(a, b): return a / b if b != 0 else "Error: Division by zero"
    @staticmethod
    def mod(a, b): return a % b if b != 0 else "Error: Modulo by zero"
    @staticmethod
    def square(a): return a ** 2
    @staticmethod
    def sqrt(a): return a ** 0.5 if a >= 0 else "Error: Negative square root"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        operation = request.form["operation"]
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0)) if operation not in ["square", "sqrt"] else 0
        except ValueError:
            result = "Invalid input"
            return render_template("index.html", result=result)

        if operation == "add":
            result = Calculator.add(num1, num2)
        elif operation == "sub":
            result = Calculator.sub(num1, num2)
        elif operation == "mul":
            result = Calculator.mul(num1, num2)
        elif operation == "div":
            result = Calculator.div(num1, num2)
        elif operation == "mod":
            result = Calculator.mod(num1, num2)
        elif operation == "square":
            try:
                result = Calculator.square(num1)
            except Exception:
                result = "Invalid input for square"
        elif operation == "sqrt":
            try:
                result = Calculator.sqrt(num1)
            except Exception:
                result = "Invalid input for square root"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)