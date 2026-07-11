correct_password = 1234

password = int(input("Enter the password: "))
while password != correct_password:
    print("Invalid password try again")
    password = int(input("Enter the password: "))
print("Password Accepted , Login Successfully")