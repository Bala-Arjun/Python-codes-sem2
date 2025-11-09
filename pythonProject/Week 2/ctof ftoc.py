def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Choose 1 or 2: ")
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    print(celsius, "°C = ", celsius_to_fahrenheit(celsius), "°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(fahrenheit, "°F = ", fahrenheit_to_celsius(fahrenheit), "°C")
else:
    print("Invalid choice.")

    