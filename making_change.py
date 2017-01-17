def my_change(total, coins):
    ways = [1] + [0]*(total)

    # Iterate over options (which coin to use now)
    for coin in coins:
        # Add the ways this coin could be added to each value from coin to the end
        for i in range(coin, total + 1):
            ways[i] += ways[i - coin]

    print ways
    return ways[total]


total = 15
coins = [1,2,3]
print my_change(total, coins)
