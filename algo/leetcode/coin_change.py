def coin_change(coins, amount):
    coins = sorted(coins, reverse=True)
    counter = 0
    for coin in coins:
        if amount == 0:
            return counter
        counter += amount // coin
        amount = amount % coin
    return -1
