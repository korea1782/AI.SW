물건의 갯수 n개와 무게 제한 C가 주어질 때, w 물건의무게가 C를 넘지 않고 가장 높은 가치 v를 가질 수 있도록 물건을 담으시오.

---
by. korea1782
```python
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n,C = map(int, sys.stdin.readline().split())
    w = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))
    T = [[0]*(C+1) for _ in range(n)]
    for i in range(n):
        for j in range(1, C+1):
            if i == 0:
                if w[i] > j:
                    T[i][j] = 0
                else:
                    T[i][j] = v[i]
            else:
                if w[i] > j:
                    T[i][j] = T[i-1][j]
                else:
                    T[i][j] = max(T[i-1][j], T[i-1][j-w[i]]+v[i])
    print(w,v)
    print(T)
    print(T[n-1][C])

```
