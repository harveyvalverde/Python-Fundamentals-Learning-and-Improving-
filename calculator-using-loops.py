#I'll try to create a very simple but functional calculator by myself, just trying to practice the commands I've learned
cont = "yes"
print("Welcome to the best calculator in world!" )
while cont == "yes":
    question = input("What operation would you like to make? '+', '-', '*', or '/': ")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
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
    cont = input("Do you want to make another operation? yes/no: ")
print("Goodbye!")
#It worked!/