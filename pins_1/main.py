"""1. Гвоздики."""

def main():
    """Решение."""
    n = int(input())
    coords = [int(i) for i in input().split()]
    coords.sort()
    dp = [0] * (n-1)

    # 2 гвоздя. Надо 2 соединить, иначе никак.
    dp[0] = coords[1] - coords[0]

    if n >= 3:
        # 3 гвоздя. Надо 3 соединить, иначе никак.
        dp[1] = coords[2] - coords[0]

    # 4 гвоздя и больше.
    for i in range(2, n-1): # NB: [2, n)
        dp[i] = min(dp[i - 1], dp[i - 2]) + coords[i + 1] - coords[i]

    print(dp[-1])


if __name__ == "__main__":
    main()
