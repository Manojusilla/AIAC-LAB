#Task-1
#Write a simple Python program to find the factorial of a number using loops, without using any functions.
import math
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)


#Task-2
#Improve the above factorial program by making the code simpler, removing extra variables, and making it easier to read.
import math
num = 
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")


#Task-3
#Write a Python program to calculate the factorial of a number using a function.
import math
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 6
print(f"Factorial of {num} is {factorial(num)}")


#Task-4
#Write a program that compares factorial code written without functions and with functions
import math
print("Factorial of 5 without function:")
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)
print("\nFactorial of 6 with function:")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 6
print(f"Factorial of {num} is {factorial(num)}")


#Task-5
#Write a program that calculates factorial using both iterative and recursive methods
import math
def iterative_factorial(n):
    """Calculate factorial using an iterative approach."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
def recursive_factorial(n):
    """Calculate factorial using a recursive approach."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
num = 7
print(f"Iterative Factorial of {num} is {iterative_factorial(num)}")
print(f"Recursive Factorial of {num} is {recursive_factorial(num)}")   