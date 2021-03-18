# 프로그래머스 2021 KAKAO BLIND RECURITMENT 메뉴리뉴얼

```python
def perm(arr,idx,N,r,sel,my_list):

    if idx == N:
        a = []
        for i in range(N):
            if sel[i]:
                a.append(arr[i])
        a.sort()
        if len(a) == r:
            my_list.append(tuple(a))
        return

    sel[idx] = 1
    perm(arr,idx+1,N,r,sel,my_list)
    sel[idx] = 0
    perm(arr,idx+1,N,r,sel,my_list)

def solution(orders, course):

    answer = []
    my_list = []

    for i in range(len(course)):
        r = int(course[i])

        for j in range(len(orders)):
            arr = orders[j]
            N = len(arr)
            sel = [0] * N
            visited = [0] * N
            perm(arr,0,N,r,sel,my_list)


    my_dict = {}
    for i in my_list:
        my_dict[i] = my_dict.get(i,0)+1

    ans = []
    for i in course:
        my_max = 0
        for k,v in my_dict.items():
            if len(k) == int(i) and v >= 2:
                if my_max < v:
                    my_max = v

        for k,v in my_dict.items():
            if len(k) == int(i):
                if v == my_max:
                    ans.append(k)


    for i in sorted(ans):
        w = ''.join(i)
        answer.append(w)

    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
```

1. 우선 주어진 orders의 갯수만큼 가능한 조합을 구한다
2. 각각의 총 갯수를 딕셔너리에 저장한다
3. 그중 최대값을 찾아서 answer에 저장한다.