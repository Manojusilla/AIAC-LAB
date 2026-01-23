# ============================================================
# Lab Assignment 4.2 – AI Assisted Coding
# Zero-shot, One-shot, and Few-shot Prompting Techniques
# ============================================================


# ------------------------------------------------------------
# Task 1: Zero-shot Prompting
# Write a function to check whether a number is prime
# ------------------------------------------------------------

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sample Output
print("Task 1 Output:")
print(is_prime(7))   # True
print(is_prime(10))  # False


# ------------------------------------------------------------
# Task 2: One-shot Prompting
# Example: Input [1,2,3,4] → Output 10
# Write a function to calculate the sum of list elements
# ------------------------------------------------------------

def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Sample Output
print("\nTask 2 Output:")
print(list_sum([1, 2, 3, 4]))  # 10


# ------------------------------------------------------------
# Task 3: Few-shot Prompting
# Extract digits from an alphanumeric string
# Examples:
# "a1b2c3" → "123"
# "abc456" → "456"
# ------------------------------------------------------------

def extract_digits(text):
    result = ""
    for char in text:
        if char.isdigit():
            result += char
    return result

# Sample Output
print("\nTask 3 Output:")
print(extract_digits("a1b2c3"))  # 123
print(extract_digits("9x8y"))    # 98


# ------------------------------------------------------------
# Task 4: Comparison – Zero-shot vs Few-shot Prompting
# Count number of vowels in a string
# ------------------------------------------------------------

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Sample Output
print("\nTask 4 Output:")
print(count_vowels("hello"))     # 2
print(count_vowels("AI Coding")) # 4


# ------------------------------------------------------------
# Task 5: Few-shot Prompting
# Find the minimum of three numbers without using min()
# Examples:
# (3,5,1) → 1
# (10,7,9) → 7
# ------------------------------------------------------------

def minimum_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

# Sample Output
print("\nTask 5 Output:")
print(minimum_of_three(3, 5, 1))    # 1
print(minimum_of_three(10, 7, 9))   # 7
    