# oop

- 객체(Object)
- 객체지향프로그래밍(Object Oriented Programing)
- 클래스(Class)와 객체(Object)

---



## 1. 객체(Object)

> Python에서 모든것은 객체이다.
>
> 모든 객체는 타입(type), 속성(attribute), 조작법(method)를 가진다.



- 타입(Type)
  - 공통된 속성(attriubte)과 조작법(method)을 가진 객체들의 분류
- 인스턴스(Instance)
  - 특정 타입(type)의 실제 데이터 예시(instance)이다.
  - 파이썬에서 모든 것은 객체이고, 모든 객체는 특정 타입의 인스턴스이다.

```python
a = 10
b = 20
# a, b 는 객체
# a, b 는 int 타입(type)의 인스턴스

isinstance(a,int)
# True
```

- 메서드(method)
  - 특정 객체에 적용할 수 있는 행위를 뜻한다.

```python
a = [1,2,3]

# 리스트 타입의 객체들이 가지고 있는 method
print(dir(a))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
```



---



## 2. 객체지향프로그래밍(Object Oriented Programing)

> 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임의 하나이다.
>
> 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다.

- 장점

  > 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용된다.
  >
  > 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며,
  >
  > 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있다.
  >
  > - 코드의 **직관성**
  > - 활용의 **용이성**
  > - 변경의 **유연성**



---



## 3. 클래스(Class)와 객체(Object)

> `type`: 공통 속성을 가진 객체들의 분류(class)

> `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드

```python
class Person():
    # 생성자 : 객체가 생성될때 호출되는 함수
    def __init__(self,name):
        self.name = name
        
    def say(self):
        print('hello my name is {}'.format(self.name))
        
p1 = Person('tom')
p1.say()
# hello my name is tom
```



- 상속

  > 클래스에서 가장 큰 특징은 상속이 가능하다는 것이다. 부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드 재사용성이 높아진다.

```python
class Student(Person):
    #자식 클래스에 메서드를 추가로 구현할 수 있다.
	# 부모 클래스의 내용을 사용하고자 할 때, super()를 사용할 수 있다.
    def __init__(self,name,student_id):
        super().__init__(name)
        self.student_id = student_id
    def talk(self):
        print('hello i am student')

s1 = Student('jimmy',2020)
s1.say()
s1.talk()
'''
hello my name is jimmy
hello i am student
2020
'''
```



