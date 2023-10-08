import sys


def main():
    def fits(a, b, hole_a, hole_b) -> bool:
        """Проверяет влезет ли кирпич в дырку."""
        result = False
        if a <= hole_a and b <= hole_b:
            result = True
        # Мы же можем повернуть кирпич на 90 град.
        if a <= hole_b and b <= hole_a:
            result = True
        return result

    # Считаем инпут. AxBxC - кирпич; D, E - дырка.
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    # Грань AxB
    if fits(a, b, d, e):
        print("YES")
        return
    # Грань BxC
    if fits(b, c, d, e):
        print("YES")
        return
    # Грань AxC
    if fits(a, c, d, e):
        print("YES")
        return
    print("NO")


if __name__ == "__main__":
    main()
