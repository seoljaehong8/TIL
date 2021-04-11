# 백준_15686 치킨배달

```python
from itertools import combinations

import sys
sys.stdin = open('input.txt','r')

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

chicken_pos = []
home_pos = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken_pos.append([i,j])
        if arr[i][j] == 1:
            home_pos.append([i,j,[]])

my_dist = []
for i in range(len(home_pos)):
    hr = home_pos[i][0]
    hc = home_pos[i][1]
    for j in range(len(chicken_pos)):
        cr = chicken_pos[j][0]
        cc = chicken_pos[j][1]

        dist = abs(hr-cr) + abs(hc-cc)

        # 자기집에서 각각의 치킨집 까지의 거리를 리스트로 저장
        home_pos[i][2].append(dist)

    # 집에서 모든 치킨집 까지의 거리 리스트
    my_dist.append(home_pos[i][2])

n = len(chicken_pos)
comb = combinations(list(range(n)),M)

ans = 1000000
for i in comb:
    a = 0
    for dist in my_dist:
        home_min = 100000
        for j in i:
            if home_min > dist[j]:
                home_min = dist[j]
        a += home_min
    if a < ans:
        ans = a

print(ans)
```

1. 각각의 집에서 모든 치킨집 까지의 거리를 구해서 `my_dist` 에 저장한다.
2. 주어진 갯수만큼 치킨집의 조합을 구한다.
3. 주어진 치킨집에서 최소값을 선택해 답을 구한다.