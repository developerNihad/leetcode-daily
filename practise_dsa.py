
# FizzBuzz Problem:

"""for num in range(1, 21):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)"""

# Sum Even Numbers between 1 and n:


"""def sum_even_numbers(n):
    sum = 0
    for num in range(1, n + 1):
        sum += num
    return sum

print(sum_even_numbers(10))"""


# Counts The Occurrences Of Each Character In A String:

"""def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

print(count_characters("salam"))"""


# Find The Largest Number In A List:

"""def find_largest_number(numbers):

    if not numbers:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

print(find_largest_number([243, 53, 245]))"""


# Second Way (built-in function)

"""def find_largest_number(numbers):

    return max(numbers) if numbers else None

print(find_largest_number([243, 53, 245]))"""


# If A String Is A Palindrome

"""def is_palindrome(string):

    string = string.lower()

    return string == string[::-1]"""


# Fibonacci Numbers

"""def generate_fibonacci(n):

    if n <= 0:
        return False
    
    elif n == 1:
        return [0]

    elif n == 2:
        return [0, 1]

    fibonacci = [0, 1]

    for i in range(2, n):
        next_number = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_number)

    return fibonacci

print(generate_fibonacci(1))
print(generate_fibonacci(2))
print(generate_fibonacci(5))"""