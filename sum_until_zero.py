total = 0

number = int(input("Enter a number (0 to stop): "))

while number!=0:

    total = total+number

    number = int(input("Enter a number (0 to stop): "))

print("Total =", total)