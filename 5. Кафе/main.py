import sys


def main():
    """
    Код программы.

    TODO: Решение неверное. Падает на закрытом тесте #3.
    """
    n = int(input())
    prices = list()
    for _ in range(n):
        price = int(input())
        prices.append(price)

    active_coupons = 0
    used_coupons = 0
    total = 0  # Все деньги
    # NB: индексы, начинаются с 0
    # todo: отсортировать в конце и +1
    used_days = []
    for i in range(len(prices)):
        # скип дней, в которые использован купон
        if i in used_days:
            continue

        # Накопим купон
        if prices[i] > 100:
            active_coupons += 1

        # Запишем сумму.
        total += prices[i]

        # Можем ли применить купоны?
        if active_coupons > 0:
            expensive_val = 0
            expensive_idx = 0
            for j in range(i+1, len(prices)):
                # скип дней, в которые использован купон
                if j in used_days:
                    continue
                if prices[j] > expensive_val:
                    expensive_val = prices[j]
                    expensive_idx = j
            # Применить купон на макс. день
            # если такой есть.
            if expensive_idx > 0:
                active_coupons -= 1
                used_coupons += 1
                used_days.append(expensive_idx)

    print(total)
    print(active_coupons, used_coupons)

    # отформатировать вывод
    print(*sorted([i+1 for i in used_days]), sep="\n")


if __name__ == '__main__':
    main()
