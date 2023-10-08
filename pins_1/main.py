import sys


def main():
    n = int(input())
    coords = sorted([int(i) for i in input().split()])
    dp = [0] * (n + 1)

    # 2 гвоздя. Надо 2 соединить, иначе никак.
    dp[0] = coords[1] - coords[0]
    # 3 гвоздя. Надо 3 соединить, иначе никак.
    dp[1] = coords[2] - coords[0]

    # 4 гвоздя и больше.
    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + coords[i] - coords[i - 1]

    print(dp[n])


if __name__ == "__main__":
    main()
