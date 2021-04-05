# SWEA_1232 사칙연산



```python
def postorder(node):
    left, right = node[0], node[1]

    if left:
        postorder((heap[left]))
    if right:
        postorder((heap[right]))

    if node[2] == '-':
        b = result.pop()
        a = result.pop()
        result.append(a - b)
    elif node[2] == '+':
        b = result.pop()
        a = result.pop()
        result.append(a + b)
    elif node[2] == '*':
        b = result.pop()
        a = result.pop()
        result.append(a * b)
    elif node[2] == '/':
        b = result.pop()
        a = result.pop()
        result.append(int(a / b))
    else:
        result.append(int(node[2]))

for tc in range(1,11):
    N = int(input())

    heap = [0]

    for i in range(1,N+1):
        my_input = list(input().split())
        temp = [0] * 4

        temp[0] = int(my_input[0])
        temp[1] = my_input[1]
        
        try:
            temp[2] = int(my_input[2])
        except:
            pass
        try:
            temp[3] = int(my_input[3])
        except:
            pass

        heap.append([temp[2],temp[3],temp[1]])

    result = []
    postorder(heap[1])
    print('#{} {}'.format(tc,result[0]))
```

1. `heap`에 주어진 데이터를 저장한다.
2. 후위순회(`postorder()`)를 하며 피연산자가 나올경우 `result`에 순서대로 인덱스 값을 저장한다.
3. 연산자가 나올경우 `result`에서 2개의 값을 `pop()` 하여 계산한후 다시 `append()` 한다.
4. 마지막 값이 저장되어 있는 `result[0]` 값을 출력