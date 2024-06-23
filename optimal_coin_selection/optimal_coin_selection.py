def optimal_coin_selection(coins, target_sum):
    n = len(coins)
    # Initialize the Opt array with a large negative value
    Opt = [[-float('inf')] * (target_sum + 1) for _ in range(n + 2)]

    # Initialize base cases
    for i in range(1, n + 1):
        Opt[i][1] = max(coins[i - 1], coins[i] if i < n else 0)

    # Fill the Opt array
    for j in range(2, target_sum + 1):
        for i in range(1, n + 1):
            if j >= coins[i - 1]:
                option1 = coins[i - 1] + min(Opt[i + 2][j], Opt[i + 1][j - 1] if j > 1 else 0)
                option2 = (coins[i] if i < n else 0) + min(Opt[i][j - 1] if j > 1 else 0,
                                                           Opt[i + 2][j - 1] if j > 1 else 0)
                Opt[i][j] = max(option1, option2)

    # Reconstruct the solution
    result = []
    i, j = 1, target_sum
    while j > 0:
        if i <= n and j >= coins[i - 1] and Opt[i][j] == coins[i - 1] + min(Opt[i + 2][j],
                                                                            Opt[i + 1][j - 1] if j > 1 else 0):
            result.append(coins[i - 1])
            j -= coins[i - 1]
            i += 2
        elif i < n:
            result.append(coins[i])
            j -= coins[i]
            i += 1
        else:
            break

    return result


# Example usage
coins = [10, 5, 1]  # Coin denominations
target_sum = 15  # Target sum

selected_coins = optimal_coin_selection(coins, target_sum)
print(f"Optimal coin selection for sum {target_sum}: {selected_coins}")
print(f"Total value: {sum(selected_coins)}")
print(f"Number of coins used: {len(selected_coins)}")
