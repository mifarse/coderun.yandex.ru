import sys


def main():

    MIN_VALUE = -1
    def calc(N, M, matrix, data):

        # Посчитана ли данное поле
        if (N, M) in data:
            return data[(N, M)]

        # Считаем вглубь

        if N-1 > 0:
            result1, path1 = calc(N-1, M, matrix, data)
        else:
            result1 = MIN_VALUE  # Максимальное возможное.

        if M-1 > 0:
            result2, path2 = calc(N, M-1, matrix, data)
        else:
            result2 = MIN_VALUE

        result = max(result1, result2) + matrix[-N][-M]
        path = path1 + ' D' if result1 > result2 else path2 + ' R'
        data[(N, M)] = result, path

        return result, path
    
    # Ввод данных.
    N, M = [int(x) for x in input().split()]
    matrix = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    # Обработка.
    result = calc(N, M, matrix, {(1,1): (matrix[-1][-1], '')})

    print(result[0])
    print(result[1][:0:-1]) # боже...

if __name__ == '__main__':
    main()