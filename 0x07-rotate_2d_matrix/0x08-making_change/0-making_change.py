#!/usr/bin/python3
"""
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """ The makeChange function """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
