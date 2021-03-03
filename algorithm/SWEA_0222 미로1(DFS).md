# SWEA_0222 미로1

```python
T = 10
 
def func():
    stack = []
    stack.append([1, 1])
 
    #상,좌,우,하
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    #현재위치
    cx = 1
    cy = 1
 
 
    while True:
        for i in range(4):
            # 다음위치
            nx = cx + dx[i]
            ny = cy + dy[i]
            if miro[ny][nx] == 0:
                stack.append([ny,nx])
            elif miro[ny][nx] == 3:
                return 1
        next = stack.pop()
        miro[cy][cx] = 9
        cx = next[1]
        cy = next[0]
 
        if stack == []:
            return 0
 
for tc in range(10):
    testcase = int(input())
    miro = []
 
    for i in range(16):
        w = list(input())
        miro.append(list(map(int,w)))
 
    print('#{} '.format(tc+1),end='')
    print(func())
```

> DFS, 스택을 이용한 길 찾기 문제이다. 미로가 주어지고 시작점과 도착점이 주어질때 시작점에서 도착점까지 가능 경로가 있는지를 판단하는 문제이다.
>
> 배열에서 1인 값은 벽이고 0인 값은 길이다.
>
> 우선 제일 처음 시작하는 위치의 노드를 스택에 추가한다. 상,하,좌,우 4방향을 모두 살피며 0인 값이 있는 노드를 스택에 추가한다. 
>
> 스택에서 제일 `pop`을 한다음 주어진 노드에 대해서 같은 행동을 반복한다. 지나간 길은 9로 표시한다.
>
> 계속해서 반복하다 도착점과 만나면 1을 반환하며 함수를 종료하고 끝까지 도착점을 만나지 못한다면(스택이 비어있다면) 0을 출력해 프로그램을 마친다.