"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오.
(리스트 split 과 슬라이싱 활용) """
a= input('주민등록번호 13자리를 작성해주세요:')
a=list(a)
print(a[6:7])
if (a[6:7]==['1']) or (a[6:7]==['3']):
    print('당신은 남자군요!')
else:
    print('당신은 여자군요!')
