## 진수 표현

> 2진수 (binary_number) = 0b10 = 2
> 8진수 (octal_number) = 0o10 = 8
> 10진수 (decimal_number) = 10 = 10
> 16진수 (hexadecimal_number) = 0x10 = 16



## 실수(float)

``` python
pi = 314e-2
print(pi) # 3.14
```

```python
3.5 - 3.12
# 0.3799999999999999

round(3.5 - 3.12 , 2)
#0.38

3.5 - 3.12 == 0.38
#False
```

``` python
a = 3.5 - 3.12
b = 0.38
abs(a-b) < 1e-10 #엄청나게 작은 수
#True

import sys
abs(a-b) <= sys.float_info.epsilon
# `epsilon` 은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
#True

import math
math.isclose(a,b)
#True
```



## 논리연산자(단축평가)

```python
'a' and 'b'
#'b'

'a' or 'b'
#'a'

vowels = 'aeiou'
('a' and 'b') in vowels
#False
#'a' and 'b' 의 결과는 'b' 이기 때문

('b' and 'a') in vowels
#True
```



## Identity

> 파이썬에서 05 부터 256까지의 id는 동일하다.

```python
a = 10
b = 10
print(a is b)	# True
print(id(a), id(b))	# 140706902312624 140706902312624
```

> 의도적으로 공백없는 알파벳 문자열도 같다

```python
a = 'hi'
b = 'hi'
print(a is b)	# True
print(id(a), id(b))	# 2528502698800 2528502698800

# 느낌표 때문에 같지 않다
a = 'hi!'
b = 'hi!'
print(a is b) 	# False
print(id(a), id(b))	# 2515523328368 2515523328496
```



## set

```python
set_a = {1, 2, 3}
set_b = {3, 6, 9}

# 차집합
set_a - set_b	# {1, 2}

# 합집합
set_a | set_b 	# {1, 2, 3, 6, 9}

# 교집합
set_a & set_b 	# {3}

```

