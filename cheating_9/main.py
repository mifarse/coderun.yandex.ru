"""
Во время контрольной работы профессор Флойд заметил, что некоторые студенты
обмениваются записками. Сначала он хотел поставить им всем двойки, но в тот день
профессор был добрым, а потому решил разделить студентов на две группы:
списывающих и дающих списывать, и поставить двойки только первым.

У профессора записаны все пары студентов, обменявшихся записками. Требуется
определить, сможет ли он разделить студентов на две группы так, чтобы любой
обмен записками осуществлялся от студента одной группы студенту другой группы.
"""

from enum import Enum

def main():
    """Алгоритм программы."""

    class Colors(Enum):
        """Маркеры для вершин графа."""
        NOT_VISITED = 0
        RED = 1
        BLUE = 2

    class SameColorException(Exception):
        """Ошибка для встречающихся одноцветных вершин графа."""

    def dfs(visited, edges, node, col=Colors.RED) -> None:
        """Модифицированный алгоритм поиска в глубину.
        
        Фактически, нам нужно определить, что перед нами только двудольные
        графы. https://bit.ly/48GclAV

        Будем проходить по графу и помечать поочередно вершины цветами. Если
        граф не двудольный, то вызвать ошибку SameColorExeption()
        """
        opposite_color = Colors.RED if col == Colors.BLUE else Colors.BLUE
        if visited[node - 1] == Colors.NOT_VISITED:
            visited[node - 1] = col
            for v1, v2 in edges:
                if v1 == node:
                    if visited[v1 - 1] == visited[v2 - 1]:
                        raise SameColorException()
                    dfs(visited, edges, v2, opposite_color)
                if v2 == node:
                    if visited[v1 - 1] == visited[v2 - 1]:
                        raise SameColorException()
                    dfs(visited, edges, v1, opposite_color)

    # Сбор данных.
    N, M = (int(x) for x in input().split())
    edges = []
    for _ in range(M):
        v1, v2 = (int(x) for x in input().split())
        edges.append((v1, v2))

    # Обработка.
    result = "YES"
    visited = [Colors.NOT_VISITED] * N
    for v in range(N):
        if visited[v] == Colors.NOT_VISITED:
            try:
                dfs(visited, edges, v+1)
            except SameColorException:
                result = "NO"
                break
    print(result)


if __name__ == "__main__":
    main()
