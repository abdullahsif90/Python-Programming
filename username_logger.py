print("Username Logger")
with open("users.txt","a") as us:
    entry = input("Enter the Username: ")
    us.write(entry)
    print("Username saved Successfully")