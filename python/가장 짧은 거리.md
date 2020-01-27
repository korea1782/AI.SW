x,y 좌표가 주어질 때, 가장 짧은 거리의 길이를 구하시오.

---
by. korea1782
```python
def score(t1,t2):
    (x1, y1) = t1
    (x2, y2) = t2
    return abs(x1-x2)+abs(y1-y2)

def rivalry(team):
    n = len(team)
    if n == 2:
        return score(team[0],team[1])
    elif n == 3:
        return min(score(team[0], team[1]), score(team[0], team[2]), score(team[1], team[2]))
    mp = team[n//2]
    md = min(rivalry(team[:n//2]), rivalry(team[n//2:]))
    for i in range(n//2):
        if team[i][0] >= mp[0]-md:
            for j in range(n//2,n):
                if team[j][0] <= mp[0]+md:
                    if abs(team[i][1]-team[j][1]) <= md:
                        md = min(md, score(team[i],team[j]))
    return md

import sys
sys.setrecursionlimit(1000000)

T = int(sys.stdin.readline())
for _ in range(T):
    M = int(sys.stdin.readline())
    team = []
    for i in range(M):
        team.append(tuple(map(int, sys.stdin.readline().split())))
    team.sort()
    print(rivalry(team))
```
