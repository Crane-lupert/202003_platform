"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오."""
w= input('삼각형의 가로길이를 입력해주세요:')
h= input('삼각형의 높이를 입력해주세요:')
def triang(w, h):
    w=float(int(w))
    h=float(int(h))
    return(w*h/2)

print('해당 삼각형의 면적은 {}입니다'. format(triang(w, h)))
