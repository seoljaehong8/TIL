# 1204

- 어려웠던점
  - dictionary 변수에 저장되있는 value 값들중 최대값을 찾고 그 최대값에 해당하는 key값 찾기



#### 수정 전

```python
	max_list = []   # 최빈값이 여러개 있는 경우 추가하기 위한 리스트
    max = 0

    # value값들을 반복하며 max값 찾기
    for score in score_dict.values():
        if max <= int(score):
            max = score

    # value 값이 max인 key값을 찾기위한 반복문      
    for score in score_dict.keys():
        if score_dict[score] == max:
            max_list.append(int(score))

    # max_list에 두개 이상의 값이 있는 경우        
    if len(max_list) > 1:
        for i in max_list:
            if max < i:
                max = i
    else:
        max = max_list[0]
    print(max)
```



#### 수정 후

```python
    max_num= max(my_dict.values())
    big = 0

    for j in score:
        if my_dict[j] == max_num and big < j:
            big = j
    print(big)
```

