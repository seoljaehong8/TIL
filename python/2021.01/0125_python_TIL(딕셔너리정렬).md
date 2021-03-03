## Dictionary 정렬

- key 값으로 정렬

```python
dict = {'A' :1,'D' :4,'C' :3,'B' :2}
sdict= sorted(dict.items())
print(sdict)
# [('A', 1), ('B', 2), ('C', 3), ('D', 4)]
# items() 함수는 key-value 쌍이 tuple로 구성된 리스트가 return 된다.

dict = {'A' :1,'D' :4,'C' :3,'B' :2}
sdict= sorted(dict.items(), reverse=True)
print(sdict)
# [('D', 4), ('C', 3), ('B', 2), ('A', 1)]
```



```python
pgm_lang = {
    "java": 20, 
    "javascript": 8, 
    "c": 7,  
    "r": 4, 
    "python": 28
} 

sorted(pgm_lang.keys())
# ['c', 'java', 'javascript', 'python', 'r']
sorted(pgm_lang.items())
# [('c', 7), ('java', 20), ('javascript', 8), ('python', 28), ('r', 4)]
pgm_lang_len = sorted(pgm_lang.items(), key = lambda item: item[0])
# [('c', 7), ('java', 20), ('javascript', 8), ('python', 28), ('r', 4)]


# 키의 길이(length)를 기준으로 오름차순 정렬
pgm_lang_len = sorted(pgm_lang.items(), key = lambda item: len(item[0]))
# [('c', 7), ('r', 4), ('java', 20), ('python', 28), ('javascript', 8)]
```



- value 값으로 정렬

```python
pgm_lang = {
    "java": 20, 
    "javascript": 8, 
    "c": 7,  
    "r": 4, 
    "python": 28
} 

pgm_lang_len = sorted(pgm_lang.items(), key = lambda item: item[1])
[('r', 4), ('c', 7), ('javascript', 8), ('java', 20), ('python', 28)]

# 내림차순
pgm_lang_len = sorted(pgm_lang.items(), key = lambda item: item[1], reverse=True)
```

- 딕셔너리를 요소로 가진 리스트에서 정렬

```python
data = [{'title': 'CLI for ordering Dominos pizza', 'upvote': 265}, 
        {'title': '100+ LeetCode solutions in Go', 'upvote': 189},
        {'title': 'Database basics: writing a SQL database from scratch in Go', 'upvote': 240},
        {'title': 'Generics in Go - How They Work and How to Play With Them', 'upvote': 248}]
result = sorted(data, key=lambda x:x['upvote'], reverse=True)
result

"""
[{'title': 'CLI for ordering Dominos pizza', 'upvote': 265},
 {'title': 'Generics in Go - How They Work and How to Play With Them',
  'upvote': 248},
 {'title': 'Database basics: writing a SQL database from scratch in Go',
  'upvote': 240},
 {'title': '100+ LeetCode solutions in Go', 'upvote': 189}]
"""
```



- 튜플을 딕셔너리로

```python
pgm_lang = {
    "java": 20, 
    "javascript": 8, 
    "c": 7,  
    "r": 4, 
    "python": 28
} 

a = sorted(pgm_lang.items(), key = lambda item: item[1], reverse=True)
```

1. 

```python
my_dict = {}
for i in a:
    my_dict.update({i[0] : i[1]})
```

2. 

```python
my_dict = dict((x,y) for x,y in a)
```

3. 

```python
# key와 value 바꾸기
my_dict = dict(map(reversed,a))
```



- 튜플 두개로 딕셔너리 만들기

```python
keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')

my_dict = dict(zip(keys,values))
```

