import turtle

drew = turtle.Turtle()

drew.hideturtle()

DIGIT_PATTERNS = {
    '0': [(0, 0), (0, 30), (30, 30), (30, 0), (0, 0)],  
    '1': [(0, 0), (10, 0), (10, 30)], 
    '2': [(0, 30), (20, 30), (20, 15), (0, 15), (0, 0), (20, 0)],  
    '3': [(0, 30), (20, 30), (20, 15), (0, 15), (0, 0), (20, 0)], 
    '4': [(0, 0), (10, 0), (10, 15), (30, 15), (30, 30)], 
    '5': [(0, 30), (20, 30), (20, 15), (0, 15), (0, 0), (20, 0)],  
    '6': [(0, 0), (0, 15), (20, 15), (20, 30), (0, 30)], 
    '7': [(0, 30), (20, 30), (20, 0)],  
    '8': [(0, 0), (20, 0), (20, 30), (0, 30), (0, 0)],  
    '9': [(0, 0), (20, 0), (20, 30), (0, 30), (0, 15)], 
}

def draw_digit(digit):
    patterns = {
        '0': [
            " ███ ",
            "█   █",
            "█   █",
            "█   █",
            " ███ "
        ],
        '1': [
            "  █  ",
            " ██  ",
            "  █  ",
            "  █  ",
            " ███ "
        ],
        '2': [
            " ███ ",
            "    █",
            " ███ ",
            "█    ",
            "█████"
        ],
        '3': [
            " ███ ",
            "    █",
            " ███ ",
            "    █",
            " ███ "
        ],
        '4': [
            "█   █",
            "█   █",
            "█████",
            "    █",
            "    █"
        ],
        '5': [
            "█████",
            "█    ",
            " ███ ",
            "    █",
            " ███ "
        ],
        '6': [
            " ███ ",
            "█    ",
            "████ ",
            "█   █",
            " ███ "
        ],
        '7': [
            "█████",
            "    █",
            "   █ ",
            "  █  ",
            " █   "
        ],
        '8': [
            " ███ ",
            "█   █",
            " ███ ",
            "█   █",
            " ███ "
        ],
        '9': [
            " ███ ",
            "█   █",
            " ████",
            "    █",
            " ███ "
        ]
    }
    return patterns.get(digit, [])

def draw_result(result, parity):
    result_str = str(int(result))
    digits = [draw_digit(d) for d in result_str]
    for row in range(5):  
        line = "  ".join(d[row] for d in digits)
        print(line)

def draw_digit_turtle(digit, start_x, start_y, scale):
    pattern = DIGIT_PATTERNS.get(digit, [])
    drew.penup()
    for point in pattern:
        drew.goto(start_x + point[0] * scale, start_y + point[1] * scale)
        drew.pendown()
    drew.penup()

def calculate(num1, num2, operation):
    operation = operation.lower()
    ops = {
        "add": num1 + num2,
        "subtract": num1 - num2,
        "multiply": num1 * num2,
        "divide": num1 / num2 if num2 != 0 else None
    }
    result = ops.get(operation)
    if result is None:
        print("Invalid operation or division by zero.")
        return None, None
    return result, "even" if result % 2 == 0 else "odd"

def reset():
    drew.clear()
    turtle.update()

def main():
    while True:
        reset()
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ")

        result_value, result_parity = calculate(num1, num2, operation)

        if result_value is not None:
            print(f"The result is: {result_value} ({result_parity})")
            draw_result(result_value, result_parity)
            scale = int(input("Enter the scale of drawing (1-10): "))
            x, y = -200, 100
            for digit in str(int(result_value)):
                draw_digit_turtle(digit, x, y, scale)
                x += 50
            drew.goto(0, -50)
            drew.write(f"The result is: {result_value} ({result_parity})", align="center", font=("Arial", 16, "normal"))

        continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
