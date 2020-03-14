""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""
a= input('첫번째 숫자를 입력해주세요:')
c= input('첫 숫자에 대해 원하는 연산기능은 무엇인가요?(덧셈, 뺄셈, 곱셈, 나눗셈)')
b= input('두번째 숫자를 입력하시오:')
a=float(int(a))
b=float(int(b))
if c=='덧셈':
    print(a+b)
elif c=='뺄셈':
    print(a-b)
elif c=='곱셈':
    print(a*b)
elif c=='나눗셈':
    print(a/b)
else:
    print('원하신 연산기능이 무엇인지 모르겠습니다')
