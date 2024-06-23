def count_payment_ways(n):
    # Initialize the Opt array
    Opt = [0] * (n + 1)

    # Base cases
    Opt[1] = 1
    if n >= 2:
        Opt[2] = 1
    if n >= 3:
        Opt[3] = 2
    if n >= 4:
        Opt[4] = 3
    if n >= 5:
        Opt[5] = 5

    # Fill the Opt array
    for i in range(6, n + 1):
        Opt[i] = Opt[i - 1] + Opt[i - 3] + Opt[i - 5]

    return Opt[n]


# Example usage
for i in range(1, 11):
    print(f"f({i}) = {count_payment_ways(i)}")

# Verify exponential growth
n = 100
result = count_payment_ways(n)
c = 3 ** (1 / 5)
lower_bound = c ** n
print(f"\nFor n = {n}:")
print(f"f(n) = {result}")
print(f"Lower bound (c^n) ≈ {lower_bound:.2e}")
print(f"f(n) >= c^n: {result >= lower_bound}")
