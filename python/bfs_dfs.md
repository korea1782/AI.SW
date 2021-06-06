
---
by. korea1782

```python
def dfs(V):
    # 방문한 경우 1, 방문하지 않은 경우 0
    visit[V] = 1
    print(V, end= ' ')
    for i in range(1, n+1):
        if visit[i]==0 and matrix[V][i]==1:
            dfs(i)

def bfs(V):
    # 방문한 경우 0, 방문하지 않은 경우 1
    queue = [V]
    visit[V] = 0
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        # 정점 V 와 연결된 (방문하지 않은) 다른 정점들을 queue에 쌓아 준다.
        for i in range(1, n+1):
            if visit[i]==1 and matrix[V][i]==1:
                queue.append(i)
                visit[i]=0
    
n, m, V = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    p, q = map(int, input().split())
    matrix[p][q] = matrix[q][p] = 1
visit = [0]*(n+1)  

dfs(V)
print()
bfs(V)
```
