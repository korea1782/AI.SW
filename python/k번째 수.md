소수들의 집합 num을 입력할 때(집합 num의 초기 입력 갯수는 n개이다.), 집합 num의 원소들을 서로 곱해서 집합에 추가해준다.
집합 num이 숫자 크기대로 배열되어 있을 경우, k번 째 숫자를 구하시오.

---
by. korea1782

```python
import heapq
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    k, n = map(int, sys.stdin.readline().split())
    num = list(set(map(int, sys.stdin.readline().split())))
    numlist = num[:]
    for _ in range(k-1):
        head = heapq.heappop(num)
        for j in range(len(numlist)):
            heapq.heappush(num, head*numlist[j])
            if head%numlist[j]==0:
                break
    print(head)
```
