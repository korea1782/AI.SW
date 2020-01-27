data와 찾으려는 숫자 query가 주어질 때, data의 몇번 째 index에 값이 저장되어 있는지 출력하시오.

---
by. korea1782

```python
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    data = list(map(int, sys.stdin.readline().split()))
    query = list(map(int, sys.stdin.readline().split()))
    answer = []

    for q in query:
        left = 0
        right = len(data)-1

        while left <= right:
            mid = (left + right)//2
            if q == data[mid]:
                answer.append(mid)
                break
            elif q < data[left] or q > data[right]:
                answer.append(-1)
                break
            else:
                if q < data[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
    print(*answer)
````
