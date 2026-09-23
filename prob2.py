# Username Validator

username = input("Enter your username: ")

if username.isalnum() and " " not in username and 5<= len(username) <= 10:
    print("Your username is valid.")
else:
    print("Invalid username.")