'''
1.
문자열의 역순이 문자열과 동일하면 팰린드롬이라고 한다.
예를 들어, "토마토"는 팰린드롬이지만, "radio"는 팰린드롬이 아니다.
문자열이 주어지면 python 함수를 작성하여 팰린드롬인지 여부를 확인하시오.

테스트코드
<입력>
print(is_palindrome("radio"))
print(is_palindrome("토마토"))

<출력>
False
True
'''
def is_palindrome(word):
    list1=list(word)
    if len(list1)%2==1:
        while len(list1)!=1:
            if list1[0]==list1[-1]:
                del list1[0]
                del list1[-1]
            else:
                return(print(False))
        print(True)
    else:
        while len(list1)!=0:
            if list1[0]==list1[-1]:
                del list1[0]
                del list1[-1]
            else:
                return(print(False))
        print(True)

word = input('팰린드룸을 검사할 단어를 적어주세요>')
is_palindrome(word)
