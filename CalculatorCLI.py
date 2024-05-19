def get_number():
  """Gets a valid number as input from the user."""
  while True:
    try:
      num = float(input("Enter a number: "))
      return num
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_operator():
  """Gets a valid operator as input from the user."""
  while True:
    operator = input("Enter an operator (+, -, *, /, ^, or sq for square root): ")
    if operator in "+-*/^sq":
      return operator
    else:
      print("Invalid operator. Please enter +, -, *, /, ^, or sq.")

def calculate(num1, operator, num2):
  """Performs the calculation based on the operator."""
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Cannot divide by zero.")
      return None
    else:
      return num1 / num2
  elif operator == "^":
    return num1 ** num2  # Power of
  elif operator == "sq":
    if num1 < 0:
      print("Error: Cannot take square root of negative number.")
      return None
    else:
      return num1**0.5  # Square root

def main():
  """Runs the calculator program."""
  print("Calculator!")
  while True:
    num1 = get_number()
    operator = get_operator()
    if operator == "sq":
      # Square root only needs one number
      result = calculate(num1, operator, None)
    else:
      num2 = get_number()
      result = calculate(num1, operator, num2)
    
    if result is not None:
      print(f"{num1} {operator} {'?' if num2 is None else num2} = {result}")

    # Ask if user wants to continue
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
      break

  print("Thanks for using Calculator!")

if __name__ == "__main__":
  main()
