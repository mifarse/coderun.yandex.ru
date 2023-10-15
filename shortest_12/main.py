"""12. Длина кратчайшего пути."""

from collections import deque


def main():
    """
    Алгоритм решения задачи.
    """
    # Сбор данных.
    N = int(input())
    adjacency_matrix = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        adjacency_matrix.append(row)
    start, finish = [int(x) for x in input().split()]

    # Обработка решения.
    visited = set()  # Посещенные вершины.
    queue = deque()  # Очередь.
    found_path = False

    queue.append((start, 0))

    while queue:
        node, depth = queue.popleft()
        # Обрабатываем только те вершины, которые не проверялись.
        if node not in visited:
            visited.add(node)

            # Проверка, если это нужная вершина.
            if node == finish:
                found_path = True
                break

            # Иначе добавим соседей в очередь.
            for i in range(N):
                if adjacency_matrix[node - 1][i]:  # Здесь либо 0, либо 1.
                    queue.append((i + 1, depth + 1))

    if found_path:
        print(depth)
    else:
        print("-1")


if __name__ == "__main__":
    main()
