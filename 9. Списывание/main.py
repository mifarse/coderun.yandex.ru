import sys


def main():
    def dfs(visited, edges, node, col=1):  #function for dfs 
        if not visited[node-1]:
            visited[node-1] = col
            for e1, e2 in edges:
                if e1 == node:
                    if visited[e1-1] == visited[e2-1]:
                        raise Exception()
                    dfs(visited, edges, e2, 1 if col==2 else 2)
                if e2 == node:
                    if visited[e1-1] == visited[e2-1]:
                        raise Exception()
                    dfs(visited, edges, e1, 1 if col==2 else 2)
    
    n, m = (int(x) for x in input().split())
    edges = []
    for i in range(m):
        e1, e2 = (int(x) for x in input().split())
        edges.append((e1,e2))
    # Обработка.

    result = "YES"
    
    visited = [0] * n
    for v in range(n):
        if not visited[v]:
            try:
                dfs(visited, edges, v+1)
            except Exception:
                result = "NO"
                break
    print(result)

if __name__ == '__main__':
    main()