"""1. 아래와 같이 숫자를 두번 물어보게 하고 ★을 출력해서 사각형을 만드시오
가로의 숫자를 입력하시오 :
세로의 숫자를 입력하시오 : """
import numpy as np
a= int(input('가로의 숫자를 입력하시오:'))
b= int(input('세로의 숫자를 입력하시오:'))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()
