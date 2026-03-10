temperature = float(input("Enter temperature: "))
value = input("Celsius(C) or Farenheit(F)?: ").lower()
if value == "c":
    F = (temperature * 1.8) + 32
    print(F)
elif value == "f":
    C = (temperature - 32) / 1.8
    print(C)
