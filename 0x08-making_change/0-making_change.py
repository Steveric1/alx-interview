#!/usr/bin/python3
"""Making change algorithm"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    makeChange is a method that determine the fewest number
    of coins needed to meet a given amount total.

    Args:
        - coins[int]: list of coins to make change
        - total(int): total amount given
    Returns:
        return fewest number of coins needed to meet total
    """

    if total == 0 or total < 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
