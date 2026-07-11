secret_number =7
number=int(input("Guess a number: "))
while number != secret_number:
    print("Wrong number try again")
    number=int(input("Again guess a number: "))
print("Hurrah you guess it right")