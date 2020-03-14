"""17. 1988년 ~ 2060년까지 중 월드컵이 개최되는 연도를 출력하시오"""
result=[]
list(result)
for i in range(1988, 2060):
    if i%4==2:
        result.append(i)
print(result)
