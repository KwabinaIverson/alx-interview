#!/usr/bin/python3
"""
Coin Change Algorithm - Dynamic Programming Approach
"""

def makeChange(coins, total):
    """Calculate the fewest number of coins needed to make a given total amount.
    
    This function uses a dynamic programming approach to solve the coin change problem.
    
    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The target amount to achieve with the minimum number of coins.
    
    Returns:
        int: The fewest number of coins needed to achieve the total amount,
        or -1 if it is not possible to reach the total with the given coins.
    """
    if total == 0:
        return 0
    if total < 0:
        return -1

    # Initialize a list to store the minimum coins required for each amount up to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Populate the min_coins array
    for coin in coins:
        for amount in range(coin, total + 1):
            if min_coins[amount - coin] != float('inf'):
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    # If min_coins[total] is still infinity, no solution was found
    return min_coins[total] if min_coins[total] != float('inf') else -1
