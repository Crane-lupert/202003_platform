"""19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오

 """
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
for i in range(len(a)):
    b=list(a[i])
    if len(b)==7:
        ''.join(b)
        print ("".join(b))
