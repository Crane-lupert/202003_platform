"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""
a= input('팩토리얼을 구하고자 하는 수를 입력해주세요:')
a= int(a)
result=1
for i in range(a):
    k=i+1
    result=result*k
    k=k+1

print(result)
