"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""
a= input('점수를 입력해주세요:')
a=float(int(a))
if a>=81:
    print('A')
elif a>=61:
    print('B')
elif a>=41:
    print('C')
elif a>=21:
    print('D')
else :
    print('F')
