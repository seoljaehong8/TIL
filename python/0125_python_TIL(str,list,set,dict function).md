## 문자열 내장함수

- `.index()` 와 `.find()`  의 차이점

```python
a = 'apple'
a.find('a')	# 0
a.index('a')# 0

a.find('p')	# 1
a.index('p')# 1

a.find('f')	# -1
a.index('f')# valueerror
```



- `.replace(old,new[, count])`

```python
z = 'zoo!yoyo!'
z.replace('o','')	# 'z!yy!'
z.replace('o','',2)	# 'z!yoyo!'
```

> 바꿀 대상 글자를 새로운 글자로 바꿔서 반환한다.
>
> count를 지정하면 해당 갯수만큼만 시행한다.



- `.strip([chars])`

```python
oh = '    oh!\n'
oh.strip()	#'oh!'
oh.lstrip()	#'oh!\n'
oh.rsrtip() #'    oh!'
```

> 특정한 문자들을 지정하면 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip),  오른쪽을 제거한다(rstrip).
>
> 지정하지 않으면 공백을 제거한다.



- `'separator'.join(iterable)`

```python
word = '배고파'
words = ['안녕', 'hello']

'!'.join(word)	# 배!고!파!
','.join(words) # 안녕,hello
```



- `.capitalize()` , `.title()` 

```python
a = 'hI! Everyone, I\'m kim'
a.capitzlize()	#"Hi! everyone, i'm kim"
a.title()		#"Hi! Everyone, I'M Kim"
```

> - `.capitalize()` : 앞글자를 대문자로 만들어 반환한다.
> - `.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환한다.



>  https://docs.python.org/ko/3/library/stdtypes.html#string-methods





### 리스트 내장 함수

`.extend(iterable)`

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.extend(['이디야','스벅','할리스'])
# ['starbucks', 'tomntoms', 'hollys', '이디야', '이디야', '스벅', '할리스']
```

> 리스트에 iterable(list, range, tuple, string**[주의]**) 값을 붙일 수가 있다.

``` python
print(cafe)
cafe.extend('ediya')
print(cafe)
'''
['starbucks', 'tomntoms', 'hollys', '이디야', '이디야', '스벅', '할리스']
['starbucks', 'tomntoms', 'hollys', '이디야', '이디야', '스벅', '할리스', 'e', 'd', 'i', 'y', 'a']
'''
```

> 반복해서 개별 요소 하나하나를 추가한다.



- `.insert(i,x)`

```python
cafe.insert(-1,'hello')			# 가장 마지막에서 한칸 앞에 추가
cafe.insert(len(cafe),'hello')	# 가장 마지막에 추가
cafe.insert(12345,'hello')		# 인덱스를 넘어서면 가장 마지막에 추가
```

> 원하는 위치에 추가



- #### 리스트 복사

```python
original_list = [1, 2, 3]
copy_list = original_list

print(copy_list)	# [1,2,3]
copy_list[0] = 'A'
print(copy_list,original_list)	# ['A', 2, 3] ['A', 2, 3]

print(id(copy_list))
print(id(original_list))
'''
1811546893952
1811546893952
'''
```

> `original_list`와 `copy_list` 의 id의 값이 같다
>
> `copy_list = original_list` => 같은 메모리 공간을 보게한다.



```python
a = [1, 2, 3, 4]
b = a[:]
b[0] = 100

print(a)
print(b)
'''
[1, 2, 3, 4]
[100, 2, 3, 4]
'''

a = [1, 2, 3, 4]
b = list(a)
b[0] = 100

print(a)
print(b)
'''
[1, 2, 3, 4]
[100, 2, 3, 4]
'''
```

> 이런 방식으로 복사가 가능하지만 이렇게 하는 것도 일부 상황에서만 하는 서로 다른 얕은 복사이다.



```python
a = [[1,2,3],2,3]
b = list(a)
print(a,b)
b[0][0] = 100
print(a,b)
b[1] = '원소'
print(a,b)

'''
[[1, 2, 3], 2, 3] [[1, 2, 3], 2, 3]
[[100, 2, 3], 2, 3] [[100, 2, 3], 2, 3]
[[100, 2, 3], 2, 3] [[100, 2, 3], '원소', 3]
'''
```

> 1차원의 리스트는 복사가 가능하지만 2차원의 리스트는 여전히 복사불가능, 2차원 리스트에서는 깊은 복사가 필요하다



```python
import copy
a = [[1,2,3],2,3]
b = copy.deepcopy(a)
print(a,b)
b[0][0] = 100
print(a,b)

'''
[[1, 2, 3], 2, 3] [[1, 2, 3], 2, 3]
[[1, 2, 3], 2, 3] [[100, 2, 3], 2, 3]
'''
```



- **List Comprehension**

```python
# 1~10까지의 숫자로 만든 세제곱 담긴 리스트 cubic_list
numbers = range(1, 11)
cubic_list = []
for number in numbers:
    cubic_list.append(number ** 3)
print(cubic_list) # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

``` python
cubic_list_1 = [number**3 for number in numbers]
print(cubic_list_1) # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```



```python
# 1~10까지의 숫자중 짝수만 담긴 리스트 even_list
even_list = []
for i in range(1, 11):
    if i % 2 == 0:
        even_list.append(i)
print(even_list)	# [2, 4, 6, 8, 10]
```

```python
even_list_1 = [i for i in range(1,11) if i % 2 ==0]
print(even_list_1) 	# [2, 4, 6, 8, 10]
```



- map(function, iterable)

```python
# numbers를 이용하여 문자열 '123'으로 변경
numbers = [1,2,3]
''.join([str(i) for i in numbers])	#'123'

list(map(str,numbers))
''.join(list(map(str,numbers)))		# '123'
```

> 순회가능한 데이터구조(iterable)으 모든 요소에 funtion을 적용한후 그 결과를 `map_object` 형태로 return 해준다.



```python
def cube(n):
    return n ** 3
numbers = [1, 2, 3]
new_numbers = list(map(cube, numbers))
print(new_numbers)	# [1,8,27]
```



- filter(function, iterable)

```python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
new_numbers = list(filter(odd, numbers))
print(new_numbers)	#[1,3]
```

> iterable 에서 function의 반환된 결과가 `True`인 것들만 구성하여 `filter object`를 반환



- zip(*iterables)

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
pair = list(zip(girls, boys))
print(pair)	# [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```

> 복수의 iterable 객체를 모아`(zip())`준다.
>
> 결과는 튜플의 모음으로 구성된 `zip object` 를 반환한다.





### Set 내장함수

- .add(elem)

```python
a = {'사과', '바나나', '수박'}
a.update(('파인애플','애플'))
print(a)	# {'바나나', '사과', '파인애플', '애플', '수박'}
a.update('apple')
print(a)	# {'l', '바나나', '사과', '파인애플', 'e', 'a', '애플', '수박', 'p'}
```





### Dictionary 내장함수

- .get(key[, default])

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict['pineapple']	# keyerror
my_dict.get('pineapple') # None return
my_dict.get('pineapple',0) # 0을 return
```

> 두번째 인자로 값을 넘겨주면 디폴드값으로 쓸 수 있다.



- .update()

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update({'banana' : '빠나나'})
my_dict	# {'apple': '사과', 'banana': '빠나나', 'melon': '멜론'}

my_dict.update(melon='메론')
my_dict	# {'apple': '사과', 'banana': '빠나나', 'melon': '메론'}
```

> 값을 제공하는 key ,value로 덮어쓴다.



```python
grades = {'john':  80, 'eric': 90, 'justin': 90}
for student in grades:
    print(student)
print(grades.keys())
print(grades.values())
print(grades.items())
'''
john
eric
justin
dict_keys(['john', 'eric', 'justin'])
dict_values([80, 90, 90])
dict_items([('john', 80), ('eric', 90), ('justin', 90)])
'''
```



- 응용(counter)

```python
# 리스트가 주어질 때, 각각의 요소의 개수를 value 값으로 갖는 딕셔너리를 만드세요.
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

count = {}
for word in book_title:
    if word in count.keys():
        count[word] += 1
    else:
        count[word] = 1
print(count)
'''
{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}
'''

count = {}
for word in book_title:
    count[word] = count.get(word,0) + 1
print(count)
'''
{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}
'''
```



- Dictionary comprehension

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
negative_blood_types = {'-' + key: value for key, value in blood_types.items()}
# negative_blood_types = {'-' + key: blood_types[key] for key in blood_types}
print(negative_blood_types)
# {'-A': 40, '-B': 11, '-AB': 4, '-O': 45}
```

```python
a = [1,2,3]
{str(n) : n for n in a}
# {'1': 1, '2': 2, '3': 3}
```

