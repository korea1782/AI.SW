pow(n,k,20200110)의 기능을 알고리즘으로 구현하시오.

---
by. korea1782

```python
def Power(n,k):
    if k == 0:
        return 1
    if k == 1:
        return n%20200110

    half = Power(n, k//2)

    if k % 2==0:
        return (half*half)%20200110
    else:
        return (half*half*n)%20200110

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    print(Power(n,k))
```
