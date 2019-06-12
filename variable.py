#변수 이름은 문자 / 숫자 / _ 언더바로 구성
import keyword
from keyword import kwlist

friend = 1
a = 10
my_name = '박진영'

#카멜 표기법
myName = '박진영'

_yourname = '박진영'
member1 = '박진수'

# 특수기호 사용 불가
# friend$ = 1
# a! = 2

# 내장된 명령어(키워드 리스트)는 변수명으로 사용 불가 e.g) def
# alt+enter = 키워드 import
# 방법1
print(kwlist)
# 방법2
print(keyword.kwlist)

# 한글 이름 변수 사용 가능
가격1 = 1000
print(가격1)











