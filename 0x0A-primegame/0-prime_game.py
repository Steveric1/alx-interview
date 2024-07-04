#!/usr/bin/python3

"""
Prime Game that calculate the winner base on the prime
number choose in the given set of numbers. 
"""


def isWinner(x, nums):
    """
    Method that determine the winner of a prime number

    Args:
        xi: s the nuber of rounds
        nums: is an array of n

    Return:
        return name of the player that won the most rounds
    """

    if x == 0 or not nums:
        return None

    Maria, Ben = 0, 0
    i = 1

    for n in nums:
        if n < 2:
            Ben += 1
            continue

        # Sieve of Eratosthenes
        prime = [True] * (n + 1)
        p = 2

        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        # Determine the winner of the round based on the count of primes
        prime_count = sum(prime)
        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    # Determine the overall winner
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
