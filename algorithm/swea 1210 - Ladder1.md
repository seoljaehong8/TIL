# swea 1210 - Ladder1

```python
for tc in range(10):

    T = int(input())

    arr = []

    for i in range(100):
        arr.append(list(map(int,input().split())))

    row = 0
    col = 0

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                row = i
                col = j

    while True:
        try:
            if arr[row][col - 1] == 1 and col - 1 >= 0:
                col -= 1
                while arr[row-1][col] != 1:
                    col -= 1
                row -= 1
            elif arr[row][col + 1] == 1:
                col += 1
                while arr[row-1][col] != 1:
                    col += 1
                row -= 1
            else:
                row -= 1
        except:
            row -= 1

        if row == 0:
            break


    print(f'#{tc+1} ',end='')
    print(col)
```

> `try - except` 문을 활용해서 인덱스 범위를 넘어갈 경우를 처리하려고 했다.
>
> 처음에는 `col - 1` 이나 `col + 1`이 인덱스 범위를 넘어갈 경우 except문으로 처리하려고 했지만 `col + 1`의 오류는 잡아내는데 `col - 1`의 오류를 못잡고 index값을 -1로 계속해서 내려갔다. 결국 그 조건만 다시 if문으로 잡아줬으며 index값이 더 큰경우는 indexerror 가 나지만 `-`로 내려갈 경우는 오류가 안뜨는걸 다시 한번 깨달았다.