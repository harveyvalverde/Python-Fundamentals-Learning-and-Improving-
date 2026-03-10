#I'll try to create a very simple but functional calculator by myself, just trying to practice the commands I've learned
question = input('Welcome to the best calculator in world! What operation do you want to do today? "+", "-", "*" or "/"?: ')
num1 = float(input("Perfect! Enter the first number: "))
num2 = float(input("Enter the second number: "))
if question == "+":
    plus = num1 + num2
    print("The result of your addition is:",plus)
elif question == "-":
    minus = num1 - num2
    print("The result of your substraction is:",minus)
elif question == "*":
    times = num1 * num2
    print("The result of your multiplication is:",times)
elif question == "/":
    divided = num1 / num2
    print("The result of your division is:",divided)
else:
    print("That's not available")
#It worked!