"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']

for i in range(len(file)):
    s=flie[i]
    sp=s.split('.')
    t=sp[0]
    result=result+t
print(result)
"""
result=[]
file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
for i in range(len(file)):
    b=file[i]
    c=b.split('.')
    d=c[0]
    result.append(d)

print(result)
