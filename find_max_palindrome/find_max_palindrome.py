def find_max_palindrome(s):
    n = len(s)
    Opt = [[False for _ in range(n)] for _ in range(n)]

    # Initialize base cases
    for i in range(n):
        Opt[i][i] = True
    for i in range(n - 1):
        Opt[i][i + 1] = (s[i] == s[i + 1])

    max_length = 1
    start = 0

    # Fill the Opt array
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            Opt[i][j] = (s[i] == s[j]) and Opt[i + 1][j - 1]

            if Opt[i][j] and length > max_length:
                max_length = length
                start = i

    return s[start:start + max_length]


# Example usage
test_strings = ["abcbea", "ABBA", "racecar", "hello"]
for s in test_strings:
    print(f"String: {s}")
    print(f"Max palindrome: {find_max_palindrome(s)}")
    print()
