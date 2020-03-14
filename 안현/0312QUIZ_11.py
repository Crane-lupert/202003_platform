"""11. 최대공약수를 구하는 함수를 구현하시오"""
a= input('최대공약수를 구하고자 하는 첫번째 수를 입력해주세요:')
a= int(a)
b= input('최대공약수를 구하고자 하는 두번째 수를 입력해주세요:')
b= int(b)
def chd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a
print(chd(a, b))
