password="python123"
user_password=input("Enter a password: ")
while user_password !=password:
    print("Invalid")
    user_password=input("Enter a password: ")
print("Login Successful")