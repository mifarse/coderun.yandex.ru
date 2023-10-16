import sys


def main():

    MAX_VALUE = 20 * 100
    def calc(N, M, matrix, data):

        # Посчитана ли данное поле
        if (N, M) in data:
            return data[(N, M)]

        # Считаем вглубь

        if N-1 > 0:
            result1 = calc(N-1, M, matrix, data)
        else:
            result1 = MAX_VALUE  # Максимальное возможное.

        if M-1 > 0:
            result2 = calc(N, M-1, matrix, data)
        else:
            result2 = MAX_VALUE

        result = min(result1, result2) + matrix[-N][-M]
        data[(N, M)] = result

        return result
    
    # Ввод данных.
    N, M = [int(x) for x in input().split()]
    matrix = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    # Обработка.
    result = calc(N, M, matrix, {(1,1): matrix[-1][-1]})

    print(result)

if __name__ == '__main__':
    main()