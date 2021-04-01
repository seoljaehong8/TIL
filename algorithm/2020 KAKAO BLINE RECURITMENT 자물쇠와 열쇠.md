# 2020 KAKAO BLINE RECURITMENT 자물쇠와 열쇠

```python
def rotate(arr):
    n = len(arr)
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = arr[n - 1 - j][i]
    return result

def check(key,lock,a,b,new_size,key_len,end):
    new_arr = [[0] * new_size for _ in range(new_size)]

    # 확장한 리스트에 key 값 넣어주기
    # 인덱스는 0,0부터 시작해서 점점 커진다
    for i in range(key_len):
        for j in range(key_len):
            new_arr[a+i][b+j] = key[i][j]

    # 확장한 리스트에 lock 값 넣어주기
    # 인덱스는 lock 이 해당하는 곳만
    for i in range(key_len - 1, end):
        for j in range(key_len - 1, end):
            new_arr[i][j] += lock[i - (key_len - 1)][j - (key_len - 1)]
            # 원래 key 값이랑 겹져치는 부분을 더했는데도 0이있거나 2가 있는경우 False
            if new_arr[i][j] == 0 or new_arr[i][j] == 2:
                return False

    return True

def solution(key, lock):

    key_len = len(key)
    lock_len = len(lock)
    # 확장할 배열 사이즈
    new_size = lock_len + ((key_len-1) * 2)
    # 키값이 검사할 마지막 인덱스 자리
    end = key_len - 1 + lock_len

    for q in range(4):
        for a in range(end):
            for b in range(end):
                if check(key,lock,a,b,new_size,key_len,end):
                    return True
        key = rotate(key)

    return False
```



1. 제일 처음 시작해야 할 부분이 key의 제일아래 오른쪽 끝부분과 lock값의 왼쪽 제일 윗 부분이다. 그만큼의 크기(`new_size`)에 해당하는 새로운 리스트를 만들어준다 (`new_arr`)
2. 새로운 사이즈로만들어진 리스트에서 key 값이 움직여 주며 lock 값과 비교하는데 그 범위는 (0,0)부터 (end,end) 까지이다.
3. `check` 함수에서 `new_arr`에 검사할 범위인 (a,b) 인덱스를 시작으로 `key_len` 만큼 key 값을 넣어준다.
4. lock 인덱스에 해당하는 범위만큼 `new_arr`리스트에 lock값에 해당하는 값을 더해준다.
5. 더했을때 해당자리가 0이거나(돌기와 홈이 안 끼워졌다면) 2라면(돌기 끼리 맞았다면) False를 리턴한다.
6. `end` 까지 검사했는데 key와 lock이 안맞다면 90도 회전후 다시 검사