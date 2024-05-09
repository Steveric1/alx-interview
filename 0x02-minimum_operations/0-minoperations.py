#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: `Copy All` and `Paste`.

@TODO:
    Deines a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
"""


def is_prime(n):
    """function to check if a number is prime or not"""
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(n):
    """function to generate prime numbers up to n"""
    prime = []
    for i in range(2, n+1):
        if is_prime(i):
            prime.append(i)
    return prime


def prime_fact(n):
    """function to generate prime factors of a number"""
    prime_factor = []
    prime = generate_prime(n)

    for i in prime:
        while n % i == 0:
            prime_factor.append(i)
            n //= i
    return prime_factor


def minOperations(n):
    """function to calculate the fewest number of operations
    needed to result in exactly n H characters in the file"""
    if n <= 1:
        return 0
    number_operations = prime_fact(n)
    sum = 0

    for operation in number_operations:
        sum += operation

    return sum
