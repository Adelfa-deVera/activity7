# Student Age Validation

try:
    age = int(input("Enter your age: "))
    if age > 18 or age < 12:
            print("Invalid age. Age must be from 12 to 18.")
    elif age >= 12 or age <= 18:
            print("Valid age.")
except ValueError:
    print("Invalid input. Please enter a whole number.")