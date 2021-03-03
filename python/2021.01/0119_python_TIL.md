# enumerate

- 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
- '열거하다' 라는 뜻이다. 
- 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환한다.
- 반복문 사용 시 몇번째 반복문이지 확인이 필요할 때 사용한다.

```python
names = ['철수','영희','길동','민수']

for i,name in enumerate(names):
    print(i+1,name)
'''
1 철수
2 영희
3 길동
4 민수
'''
```



- 세기 시작할 숫자를 정할 수 있다.

```python
for i,name in enumerate(names,10):
    print(i+1,name)
'''
11 철수
12 영희
13 길동
14 민수
'''    
```



# eval

- eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결과값을 돌려주는 함수이다.
- 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.

```python
print(eval('1+2'))
# 3
print(eval("'hi' + 'a'"))
# hia
print(eval('divmod(4, 3)'))
# (1,1)
```

