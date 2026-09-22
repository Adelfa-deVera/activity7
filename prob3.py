# Problem 3: School Grade Level Validator

lvl = (7,8,9,10,11,12)

try:
    gradelvl = int(input("Enter your grade level: "))
    if gradelvl in lvl:
        print("Valid grade level.")
    else:
        print("Invalid grade level.")

except ValueError:
    print("Invalid input. Please enter a whole number.")