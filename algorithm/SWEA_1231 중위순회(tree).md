# SWEA_1231 중위순회



```python
def inorder(node):
    if node[0]:
        inorder(heap[node[0]])
    result.append(node[2])
    if node[1]:
        inorder(heap[node[1]])

for tc in range(1,11):
    N = int(input())

    heap = [0]

    for i in range(1,N+1):
        my_input = list(input().split())

        try:
            left = int(my_input[2])
        except:
            left = 0
        try:
            right = int(my_input[3])
        except:
            right = 0

        data = i
        word = my_input[1]

        heap.append([left,right,data,word])

    result = []
    inorder(heap[1])

    print('#{} '.format(tc),end='')
    for i in result:
        print(heap[i][3],end='')
    print()
```

1. `heap`에 주어진 데이터를 저장한다.
2. 중위순회(`inorder()`)를 하며 `result`에 순서대로 인덱스 값을 저장한다.
3. `result`의 값을 이용하여 `heap`에 저장되어있는 문자를 출력한다.