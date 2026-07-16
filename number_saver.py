print("Number Saver")

# Save Numbers
with open("numbers.txt", "a") as num:
    data_entry = int(input("How many numbers you want to enter? "))

    for i in range(data_entry):
        number = input(f"Enter the number {i+1}: ")
        num.write(number + "\n")

# Read Updated File
with open("numbers.txt", "r") as num:
    print("\nUpdated Numbers:")
    print(num.read())

print("All Numbers Saved Successfully")