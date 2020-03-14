"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오."""
a= input('대소문자를 바꿀 영어알파벳을 넣어주세요:')
#list(a)
#print(a)
#for i in range(len(a)):
for i in range(len(a)):
    b=a[i:i+1]
    if b.isupper()==True:
        b=b.lower()
        print(b, end='')
    elif b.islower()==True:
        b=b.upper()
        print(b, end='')
    else:
        b='입력 형식이 잘못되었습니다'
        print(b)
