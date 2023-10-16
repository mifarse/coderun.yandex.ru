import sys


def main():

    def calc(N, M, data={ (1,1): 1}):
        
        # Посчитана ли данное поле
        if (N, M) in data:
            return data[(N, M)]

        if (M, N) in data:
            return data[(M, N)]

        # Считаем вглубь

        if N-2 > 0 or M-1 > 0:
            result1 = calc(N-2, M-1, data)
        else:
            result1 = 0

        if N-1 > 0 or M-2 > 0:
            result2 = calc(N-1, M-2, data)
        else:
            result2 = 0

        result = result1 + result2
        data[(N, M)] = result

        return result
    
    # Ввод данных.
    N, M = [int(x) for x in input().split()]

    # Обработка.
    result = calc(N, M)

    print(result)

if __name__ == '__main__':
    main()