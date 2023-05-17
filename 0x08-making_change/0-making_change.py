#!/usr/bin/python3
""" Making change """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total
    parameters:
        coins [list or positive ints]:
            the values of the coins in your possession
            you can assume you have an infinite number of coins of all values
        total [int]:
            total amount of change to make
            if total is 0 or less, return 0
    returns:
        the fewest number of coins to make the change
        or -1 if the total change cannot be made with the given coins
    """

    if total <= 0:
        return 0
    else:
        from math import trunc

        coins = sorted(coins, reverse=True)
        coin_dict = {}
        while total is not None:
            for c in coins:
                if total % c == 0:
                    coin_dict[c] = total / c
                    return(int(sum(coin_dict.values())))
                else:
                    coin_dict[c] = trunc(total / float(c))
                    total -= (c * coin_dict[c])
            return -1
