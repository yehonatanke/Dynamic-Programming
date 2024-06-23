def count_solutions(coefficients, b):
    n = len(coefficients)

    # Initialize the Opt array
    Opt = [[0 for _ in range(b + 1)] for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        Opt[i][0] = 1

    for j in range(1, b + 1):
        Opt[1][j] = 1 if j % coefficients[0] == 0 else 0

    # Fill the Opt array
    for i in range(2, n + 1):
        for j in range(1, b + 1):
            k = 0
            while k * coefficients[i - 1] <= j:
                Opt[i][j] += Opt[i - 1][j - k * coefficients[i - 1]]
                k += 1

    return Opt[n][b]


# Example usage
coefficients = [1, 2]
b = 3
result = count_solutions(coefficients, b)
print(f"Number of solutions for 1x₁ + 2x₂ = 3: {result}")

coefficients = [1, 2, 3]
b = 5
result = count_solutions(coefficients, b)
print(f"Number of solutions for 1x₁ + 2x₂ + 3x₃ = 5: {result}")
