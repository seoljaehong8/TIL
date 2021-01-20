# 매개변수 / 인자

```python
def func(x):
    return x + 2

print(func(2))
```

- 매개변수
  - `x` 는 매개변수
  - 입력을 받아 함수 내부에서 활용할 변수
  - 함수의 정의 부분에서 볼 수 있다.
- 인자
  - `2` 는 (전달)인자 (argument)
  - 실제로 전달되는 `입력값` 이라고 볼 수 있다.
  - 함수를 호출하는 부분에서 볼 수 있다.



## 함수의 인자

```python
def func(num1 = 123, num2):
    print(num1 + num2)
```

> 기본 인자값(default argument value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없다.

```python
def func(num1, num2 = 123):
    print(num1 + num2)
```

> 기본 값이 없는 인자다음에 기본 인자값을 가지는 인자는 올 수 있다.



# 재귀함수(피보나치)

```python
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_loop(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return b

import time

t0 = time.time()
fib(31)
t1 = time.time()

total = t1 - t0
print(total)	#0.29259395599365234

t0 = time.time()
fib_loop(30000)
t1 = time.time()

total = t1 - t0
print(total)	#0.009914875030517578
```

> 많은 함수 호출이 일어나야할 경우 재귀함수보다 반복문이 더 효율적이다.