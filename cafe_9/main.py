import sys
from collections import namedtuple

def main():
    
    MAX_VALUE = 300 * 100

    class Obj:
        def __init__(self, price, active_coupons):
            self.price = price
            self.active_coupons = active_coupons

        def __repr__(self):
            return f"Obj({self.price!r}, {self.active_coupons!r})"

    # Obj = namedtuple("Obj", ("price", "active_coupons"))

    n = int(input())
    prices = []
    for i in range(n):
        prices.append(int(input()))
    
    dp = []
    for i in range(n):
        row = [Obj(MAX_VALUE, []) for _ in range(i+2)]
        dp.append(row)

    if prices[0] > 100:
        dp[0][1].price = prices[0]
    else:
        dp[0][0].price = prices[0]

    active_coupons = []

    # TODO: где-то не сохраняются купоны.

    for i in range(1, n):
        if prices[i] > 100:
            dp[i][1].price = dp[i-1][0].price + prices[i]
            dp[i][1].active_coupons = dp[i-1][0].active_coupons
        else:
            dp[i][0].price = dp[i-1][0].price + prices[i]
            dp[i][1].active_coupons = dp[i-1][0].active_coupons
        for j in range(1, i+1):
            
            if dp[i-1][j].price < dp[i][j-1].price:
                dp[i][j-1].price = dp[i-1][j].price
                dp[i][j-1].active_coupons.append(i+1)


            if prices[i] > 100:
                dp[i][j+1].price = dp[i-1][j].price + prices[i]
            else:
                dp[i][j].price = dp[i-1][j].price + prices[i]

    result = MAX_VALUE
    count_of_coupons = 0
    active_coupons = []
    for j, x in enumerate(dp[n-1]):
        if x.price < result:
            result = x.price
            count_of_coupons = j
            active_coupons = x.active_coupons


    print(dp)
    print(result)
    print(count_of_coupons, len(active_coupons))
    for x in active_coupons:
        print(x)

if __name__ == "__main__":
    main()
