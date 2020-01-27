한 사람이 사다리를 1번에 한 칸, 두 칸, 세 칸 움직일 수 있을 때, 사다리 N칸을 움직이는 경우의 수를 1904101441로 나눈 나머지를 구하라.

---

by. korea1782
```python
import sys
def Power(n):
    if n < 1904101441:
        return n
    else:
        return n%1904101441

def bridge(k):
    br = [1,2,4]
    if k == 1:
        return br[0]
    elif k == 2:
        return br[1]
    elif k == 3:
        return br[2]
    if k > 3:
        for i in range(4, k+1):
            temp = Power(br[0]+br[1]+br[2])
            br[0] = br[1]; br[1] = br[2]
            br[2] = temp
    return br[2]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print((bridge(N)))

```
