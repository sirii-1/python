def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

fact_result = factorial(5)
print("Factorial of 5:", fact_result)

fib_sequence = [fibonacci(i) for i in range(8)]
print("First 8 Fibonacci numbers:", fib_sequence)