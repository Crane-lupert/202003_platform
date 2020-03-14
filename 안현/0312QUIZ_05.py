"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""
N= input('구구단 몇 단이 보고싶나요?')
N=int(N)
print('구구단 {}단은 다음과 같습니다.'.format(N))
print('{}*1={}'.format(N, N*1))
print('{}*2={}'.format(N, N*2))
print('{}*3={}'.format(N, N*3))
print('{}*4={}'.format(N, N*4))
print('{}*5={}'.format(N, N*5))
print('{}*6={}'.format(N, N*6))
print('{}*7={}'.format(N, N*7))
print('{}*8={}'.format(N, N*8))
print('{}*9={}'.format(N, N*9))

#while함수를 이용해서 할 경우
i=int(1)
while i<10:
    print('{}*{}={}'.format(N, i,  N*i))
    i=i+1
