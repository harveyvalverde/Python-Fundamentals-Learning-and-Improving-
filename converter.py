temperature = float(input("Enter temperature: "))
#If we use "float", we'll be able to enter decimal numbers and integers, so we prevent errors
value = input("Is it Celsius(C) or Farenheit(F)?: ").upper() #Using parentheses after a method it's basically a must, if you don't, the command will just not run
if value == "F":
    celsius = (temperature - 32) * 5/9
    print(celsius)
elif value == "C":
    farenheit = temperature * 1.8 + 32
    print(farenheit)
else:
    print("Not found")
