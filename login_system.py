username="admin"
password="1234"
name=input("Enter the username: ")
code=input("Enter the password: ")


if(name==username and code==password):
    print("Login successful")
else:
    print("Invalid credentials")