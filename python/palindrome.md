문자열이 입력될 때, 팰린드럼 문자열을 이루는 최대 문자의 갯수를 출력하시오.

---
by. korea1782
```python
import sys
N = int(sys.stdin.readline())
for _ in range(N):
    string = list(sys.stdin.readline().strip())
    T = [[0]*(len(string)) for _ in range(len(string))]
    for j in range(len(string)):
        for i in range(j,-1,-1):
            if i == j:
                T[i][j] = 1
            else:
                if string[i] == string[j]:
                    T[i][j] = T[i+1][j-1]+2
                else:
                    T[i][j] = max(T[i+1][j], T[i][j-1])
    print(T[0][len(string)-1])
```
