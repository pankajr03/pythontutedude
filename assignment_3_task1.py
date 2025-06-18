def factorial(n):
    if n < 2 :
        return n
    else:
        return n * factorial(n - 1)

entered_number = int(input("Enter a number: "))

print(f'Factorial of {entered_number} is: ' + str(factorial(entered_number)))
