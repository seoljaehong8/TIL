- python에서 사용할수 없는 식별자(예약어)를 작성하시오

  > False, True, None, and, or, in, is, break, continue, for, not, try, while

```python
import keywork
print(keyword.kwlist)
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
```



- python은 부동소수점 방식을 이용하여 실수(float)를 표현하는 과정에서, 나타내고자 하는 값과의 오차가 발생하여 원하는 대로 연산 또는 비교가 되지 않을 때가 있다. 이를 참고하 여, 아래와 같은 두 실수 값을 올바르게 비교하기 위한 코드를 작성하시오.

```python
num1 = 0.1 * 3
num2 = 0.3
#1
abs(num1 - num2) <= 1e-10

#2
import sys
abs(num1 - num2) <= sys.float_info.epsilon

#3
import math
math.isclose(num1,num2)
```



- 주어진 컨테이너들을 각각 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

  > Mutable : list,dict,set Immutable :String, tuple, range



- Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

  > print(), len(), sum(), max(), min(),sorted()



- Python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.

  > local - enclosed - global - built-in



- 재귀함수를 사용했을 때 얻을 수 있는 장점과 단점을 반목문과 비교하여 작성하시오.

  > **장점**
  >
  > 알고리즘 자체가 재귀적으로 표현하기 자연스러울 때. (가독성 이야기)
  >
  > 변수 사용을 줄여 준다.

  > **단점**
  >
  > 메모리를 많이 차지하며 성능이 반복문에 비해 느리다



- 다음 중, 문자열(string)을 조작하는 방법으로 옳지 않은 것을 고르시오.

```python
(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.
(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를
기준으로 나누어 list로 반환한다. 특정 문자를 지정하지 않으면
공백을 기준으로 나눈다.
(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로
바꿔서 반환한다.
(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를
찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다.
```



- 아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

  > **init** : 어떤 클래스의 인스턴스가 생성될 때 파이썬 인터프리터에 의해 자동으로 호출되는 메소드
  >
  > **del** : 객체가 없어질때 호출되는 메소드
  >
  > **str** : 객체를 이해하기 쉽게 표현할 수 있는 문자열이다. repr보다 사용자에게 보기 쉬운 문자열을 출력하는 것에 지향점이 있다. string타입의 문자열을 반환해야 한다. repr만 구현되어있고 str이 구현되어 있지 않은 경우에는 str()이 을 불러오게 된다.
  >
  > **repr** :객체를 나타내는 공식적인 문자열이다. 반환값의 타입은 string이어야 한다. str하고 달리 좀 더 명확함을 지향하고 있는 느낌.



- ### 시퀀스(sequence) , 비 시퀀스형(Non-sequence) 분류

  > **list, dictionary, tuple, range, set**

- ### mutable(변경 가능한), imutable(변경 불가능한) 분류

  > **number, list, range,tuple, dic, set, string, bool  **

- 삼항 연산자(조건 표현식)

  > ```python
  > num = 2
  > if num % 2:
  >     result = '홀수입니다.'
  > else:
  >     result = '짝수입니다.'
  > print(result)
  > ```
  >
  > ```python
  > # 삼항 연산자로 
  > 
  > 
  > ```
  >
  > 

- while문을 이용하여 '그만' 이라는 단어가 입력되면 그전까지 입력했던 문자열을 저장후 출력

  > ```python
  > 
  > ```

- 나이가 입력된 리스트가 있을때, 조건문과 반복문, continue를 활용하여 20살 이상일때만 "성인입니다"라는 출력을 하는 코드를 작성하세요

  > ```python
  > ages = [10, 23, 8, 30, 25, 31]
  > 
  > '''
  > [출력 예시]
  > 
  > 23 살은 성인입니다.
  > 
  > 30 살은 성인입니다.
  > 
  > 25 살은 성인입니다.
  > 
  > 31 살은 성인입니다.
  > '''
  > ```

- pass 와 continue의 차이??

  > 

- 함수에서 매개변수와 인자의 차이점??

  > 

- 다음중 틀린것은?

  > ```python
  > # 1
  > def greeting(name='익명', age):
  >     print(f'안녕? 난{name}, {age}살이야')
  > # 2
  > def greeting(age, name='익명'):
  >     print(f'안녕? 난{name}, {age}살이야')
  > # 3
  > greeting(name='길동', age=1000)
  > # 4
  > greeting(age=3000, '곰')
  > # 5
  > def students(*args, prof):
  > # 6
  > dict(name='홍길동', age='1000')
  > # 7
  > dict(1='1', 2='2')
  > ```
  >
  > 

- 이거 나올삘 순서

  - `L`ocal scope: 정의된 함수

  - `E`nclosed scope: 상위 함수

  - `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈

  - `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

- 재귀함수의 장단점??

  > 

- .find(x) 와 .index(x)의 차이점?

  > 

- .append() 와 extend()의 차이점?

  > 

- .remove(i) 와 pop(i)의 차이점?

  > 

- a 에 저장되는 값들은?

  > ```python
  > a = [number**3 for number in numbers]
  > # 답 : 
  > 
  > a = [i for i in range(1, 11) if i % 2 == 0]
  > # 답 : 
  > ```

- 다음중 맞는 표현은?

  > ```python
  > # 1.
  > ['홀수' if i % 2 == 1 else '짝수' for i in range(1, 11)]
  > # 2.
  > ['홀수' for i in range(1, 11) if i % 2 == 1 else '짝수']
  > ```

- ## Object 중심의 장점

  **<wikipedia - 객체지향 프로그래밍>**

  > 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용된다.
  >
  > 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며,
  >
  > 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있다.

  - 코드의 **직관성**
  - 활용의 **용이성**
  - 변경의 **유연성**

























