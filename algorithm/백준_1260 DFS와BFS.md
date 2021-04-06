# 백준_1260 DFS와BFS

```python
import sys
sys.stdin = open('input1.txt','r')

def dfs(v):
    visited[v] = 1
    print(v,end=' ')

    for i in range(1,N+1):
        if visited[i]==0 and arr[v][i]:
            dfs(i)

    # stack.append(v)
    #
    # while stack:
    #     node = stack.pop()
    #     if visited[node] == 0:
    #         visited[node] = 1
    #         print(node, end=' ')
    #
    #     a = []
    #     for i in range(1,N+1):
    #         if visited[i] == 0 and arr[node][i]:
    #             a.append(i)
    #
    #     a.sort(reverse=True)
    #
    #     stack.extend((a))

def bfs(v):
    queue.append(v)
    visited[v] = 1
    while queue:
        node=queue.pop(0)
        print(node, end=' ')

        for i in range(1,N+1):
            if visited[i] == 0 and arr[node][i]:
                queue.append(i)
                visited[i] = 1


N,M,V = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]


stack = []
queue = []

for i in range(M):
    s,e = map(int,input().split())

    arr[s][e] = 1
    arr[e][s] = 1

visited = [0]*(N+1)
dfs(V)
print()
visited = [0]*(N+1)
bfs(V)
```

