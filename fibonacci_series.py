def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        next = a + b
        a = b
        b = next

terms = int(input("Enter number to find fibonacci: "))

fibonacci(terms)