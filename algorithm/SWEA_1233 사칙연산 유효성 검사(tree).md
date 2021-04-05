# SWEA_1233 사칙연산 유효성 검사



```python
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
    ans = 1
    for i in range(1,len(heap)):
        left = heap[i][0]
        right = heap[i][1]
        data = heap[i][2]

        # 리프노드인데 숫자가 아닐경우
        if left == 0 and right == 0:
            if data in ['-','+','/','*']:
               ans = 0

        # 자식노드가 있는데 숫자일 경우
        else:
            if data not in ['-','+','/','*']:
                ans = 0

    print('#{} {}'.format(tc,ans))
```

1. `heap`에 주어진 데이터를 저장한다.
2. 주어진 식이 유효성 검사를 통과하지 못하는 경우는 2가지로 나뉜다
   1. 리프노드인데 숫자가 아닐경우
   2. 자식노드가 있는데 연산자가 아닌 피연산자일 경우
3. 두개의 조건에 맞을 경우 `ans`값을 0으로 저장하고
4. `ans`값 출력