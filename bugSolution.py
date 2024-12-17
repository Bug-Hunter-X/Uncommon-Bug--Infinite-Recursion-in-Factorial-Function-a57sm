def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

try:
    number = -5
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
except ValueError as e:
    print(f"Error: {e}")

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
