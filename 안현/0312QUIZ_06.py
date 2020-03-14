"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""
a= input('숫자를 입력하세요:')
a=int(a)

for i in range(a*2):
    k=abs(a-i)
    for j in range(a):
        if j >= k:
            print('*', end='')
        else:
            print(' ', end='')
    print()
