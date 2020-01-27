단방향 BFS

---
by. korea1782
```
import collections
import sys
sys.setrecursionlimit(1000000)

T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int, sys.stdin.readline().split())
    List = [[] for _ in range(N)]
    for i in range(M):
        u,v = map(int, sys.stdin.readline().split())
        List[u].append(v)

    for i in range(N):
        List[i].sort()

    Check = [False]*N
    queue = collections.deque([0])
    while queue:
        v = queue.popleft()
        if Check[v] == True:
            continue
        Check[v] = True
        print(v, end=" ")
        queue.extend(List[v])

    print("")
```
