# BFS

### Queue

> `front` , `rear` 을 이용한 Queue

```python
SIZE = 100
Q = [0] * SIZE 
front, rear = -1, -1
def isFull():
    return rear == (len(Q) - 1)
def isEmpty():
    return rear == front
def enQueue(item):
    global rear
    if isFull() : print("Queue is Full")
    else:
        rear += 1
        Q[rear] = item
def deQueue():
    global front
    if isEmpty() : print("Queue is Empty")
    else:
        front += 1
        return Q[front]
def Qpeek():
    return Q[front + 1]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
```

> `list` 를 이용한 Queue

```python
Q = []

Q.append(1)
Q.append(2)
Q.append(3)

print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))
if len(Q) != 0:
    print(Q.pop(0))
```

> `queue` 모듈을 이용한 Queue

```python
import queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())
```

> `collections`모듈의 `deque`를 이용한 Queue

```python
import collections
deq = collections.deque()

deq.append(1)   #enQueue
deq.append(2)
deq.append(3)

print(deq.popleft())    #deQueue
print(deq.pop())
```

> 원형큐

```python
SIZE = 4
Q = [0] * SIZE
front, rear = 0,0
def isFull():
    # if rear == len(Q) - 1
    return (rear + 1) % SIZE == front
def isEmpty():
    return rear == front
def enQueue(item):
    global rear
    if isFull() : print("Queue is Full")
    else:
        rear = (rear + 1) % SIZE
        Q[rear] = item
def deQueue():
    global front
    if isEmpty() : print("Queue is Empty")
    else:
        front = (front + 1) % SIZE
        return Q[front]
def Qpeek():
    return Q[(front + 1) % SIZE]

enQueue(1)
print(deQueue())
enQueue(2)
print(deQueue())
enQueue(3)
print(deQueue())
enQueue(4)
enQueue(5)
enQueue(6)
print(Qpeek())
```

> BFS 를 이용한 길 찾기

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v):
    # v를 enqueue(visited 체크)
    Q.append(v)
    visited[v] = 1
    print(v, end=' ')

    # Q가 not empty:
    while Q:
        # t <- dequeue
        t = Q.pop(0)
        # t에 인접한 모든 정점 w에 대해서
        for w in range(1,V+1):
            # w가 not visited이면
            if adj[t][w] == 1 and visited[w] == 0:
                # enqueue
                Q.append(w)
                visited[w] = visited[t] + 1
                print(w,end=' ')

V,E = map(int,input().split())  #정점, 간선
temp = list(map(int,input().split()))
adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬
Q = []
visited = [0] * (V+1)

# 인접행렬 입력
for i in range(E):
    s, e = temp[2*i], temp[2*i + 1]
    # 무향그래프
    adj[s][e] = 1
    adj[e][s] = 1

bfs(1)
print()
print(visited)
```



