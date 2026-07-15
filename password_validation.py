print("***Password Creater***")
create_password = input("Enter the password (8 characters minimum): ")


def validate_password(password):
        if len(create_password) < 8:
            print("Invalid Password")
            return
        print("Valid Password")
        print("\n***Login System***")
        login_password = input("Enter the password: ")
        if login_password == password:
            print("Login Successful")
        else:
            print("Incorrect Password")

validate_password(create_password)
