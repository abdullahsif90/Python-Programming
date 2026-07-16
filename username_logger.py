print("Username Logger")
with open("users.txt","a") as us:
    entry = int(input("how many username? "))
    for i in range(entry):
        username = input(f"Enter the username no {i+1}: ")
        us.write(username + "\n") # \n for to entry in next line 
    print("Username saved Successfully")
