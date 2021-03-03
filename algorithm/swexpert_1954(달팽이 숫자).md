# SWEA 1954.

### 달팽이 행렬

![image-20210121202023700](C:\Users\Hong_laptop\AppData\Roaming\Typora\typora-user-images\image-20210121202023700.png)

```python
def my_func(T):
    for i in range(T):

        N = int(input())	# N x N 행렬
        printN = N		#마지막 출력을 위한 변수

        cnt = 1		#행렬에 담길 숫자
        plus = 1	#행렬의 위치를 이동시킬 변수

        i = 0	#행
        j = -1	#열

        my_list = [[0 for i in range(N)] for j in range(N)]

        while N > 0:

            for a in range(N):
                j += plus
                my_list[i][j] = cnt
                cnt += 1

            N -= 1

            for b in range(N):
                i += plus
                my_list[i][j] = cnt
                cnt += 1

            plus *= -1

        for i in range(printN):
            for j in range(printN):
                print('{:02}'.format(my_list[i][j]),end=' ')
            print()

        print()


T = int(input())
my_func(T)
```



>  우선 4x4 행열을 생각해보자. 처음에는 열값(`j`) 만을 <u>**증가**</u> 시키며 (0,0) , (0,1) , (0,2) , (0,3) 까지 4번의 숫자를 행렬에 넣는다. 여기서는 이중리스트로 표현하였다.
>
>  그다음은 행값(`i`)만을 <u>**증가**</u>시키며 (1,3) , (2,3) , (3,3) 3번의 숫자를 행렬에 넣는다.
>
> 그다음은 열값(`j`)을 <u>**감소**</u>시키며 3번의 숫자를 넣고
>
> 행값(`i`)을 <u>**감소**</u>시키며 2번의 숫자를 넣는다.
>
> 행렬에 숫자를 넣는 횟수가 줄어드므로 `N -= 1` 
>
> 행,열 값이 증가도 하고 감소가 필요한 부분도 있으므로 `plus *= -1` 



- 잘 풀리지 않을때는 그림을 그려가며 풀이법을 찾으면 좀더 수월하게 찾을 수 있다.