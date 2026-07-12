print("Registration System \n")

username = input("Create a username: ")

password = int(input("Create a password (positive integer): "))

while password <= 0:
    print("Password must be a positive number.")
    password = int(input("Create a password (positive integer): "))

print("\n Login System")

attempts = 0

while attempts < 3:

    login_username = input("Enter username: ")
    login_password = int(input("Enter password: "))

    if login_username == username and login_password == password:
        print("Login Successful")
        break

    else:
        attempts += 1
        print("Invalid Username or Password")
        print("Remaining Attempts:", 3 - attempts)

if attempts == 3:
    print("Account Locked")