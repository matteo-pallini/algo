def coin_change_two(coins, amount):
    """
    read about the knapsack problem

    insane solution. Each amount can be built by each coin and whatever other
    complementary value, ie coin == 2 + complementary == 3 gives 5.
    So, we need to compute how many other values give the complementary 3
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]]
