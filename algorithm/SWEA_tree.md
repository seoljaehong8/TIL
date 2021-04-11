# SWEA_5174_subtree

```python
import sys
sys.stdin = open('5174_input.txt','r')

def postorder(node):
    global ans
    if node == 0:
        return
    postorder(left[node])
    postorder(right[node])
    ans += 1


T = int(input())

for tc in range(T):
    E,N = map(int,input().split())

    temp = list(map(int,input().split()))

    left = [0]*(E+2)
    right = [0] * (E+2)

    for i in range(E):
        parent = temp[2*i]
        child = temp[2*i+1]
        if left[parent]:
            right[parent] = child
        else:
            left[parent] = child

    ans = 0
    postorder(N)
    print('#{} {}'.format(tc+1,ans))


'''
def postorder(node):
    global ans
    if node[0]:
        postorder(arr[node[0]])
    if node[1]:
        postorder(arr[node[1]])
    ans += 1


T = int(input())

for tc in range(T):
    E,N = map(int,input().split())

    temp = list(map(int,input().split()))

    arr = [[] for _ in range(E+2)]

    for i in range(E):
        parent = temp[2*i]
        child = temp[2*i+1]
        arr[parent].append(child)

    for i in range(E+2):
        while len(arr[i]) != 2:
            arr[i].append(0)

    ans = 0
    postorder(arr[N])
    print('#{} {}'.format(tc+1,ans))
'''
```

# SWEA_5176 이진탐색

```python
import sys
sys.stdin = open('5176_input.txt','r')

def inorder(node):
    global cnt
    if node <= N:
        inorder(node * 2)
        tree[node] = cnt
        cnt += 1
        inorder(node * 2 + 1)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    cnt = 1
    inorder(1)
    print('#{} {} {}'.format(t, tree[1], tree[N//2]))
```

# SWEA_5177 이진힙

```python
import sys
sys.stdin = open('5177_input.txt','r')

def my_sort(idx):
    if idx > 1:
        if heap[idx] < heap[idx//2]:
            heap[idx],heap[idx//2] = heap[idx//2],heap[idx]
            my_sort(idx//2)

def my_add(data):
    global idx
    idx += 1
    heap[idx] = data
    my_sort(idx)

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int,input().split()))

    heap = [0] * (N+1)
    idx = 0

    for i in range(N):
        my_add(data[i])

    p_node = []
    while N > 1:
        N //= 2
        p_node.append(N)

    ans = 0
    for i in p_node:
        ans += heap[i]
    print('#{} {}'.format(tc+1,ans))
```

# SWEA_5178 노드의 합

```python
import sys
sys.stdin = open('5178_input.txt','r')

def postorder(node):
    global ans
    if node<=N:
        postorder(left[node])
        postorder(right[node])
        ans += heap[node]

T = int(input())

for tc in range(T):
    N,M,L = map(int,input().split())

    left = [0]
    right = [0]
    heap = [0] * (N+1)

    for i in range(M):
        temp = list(map(int,input().split()))
        idx = temp[0]
        data = temp[1]
        heap[idx] = data

    for i in range(1,N+1):
        left.append(2*i)
        right.append(2*i+1)

    ans = 0
    postorder(L)
    print('#{} {}'.format(tc+1,ans))
```

