# 치환문 예시
a = 1
b = a+1

# 함수 아니어도 순차적으로 출력 가능
print(a,b, sep=':')

# 세미 콜론으로 치환문 구분 가능
# e = 3.5: f = 5.3
# print(e,f)

# 여러 변수 한번에 치환
e, f = 3.5, 5.3
print(e, f)

# 같은 값을 여러 변수에 대입 시
# c 스타일은 지원 X
x=y=z=10
print(x,y,z)

# 현재 변수의 클래스 타입(자료형) 표시
# a의 경우 int
# 값으로 부여되는 정수 / 문자열 등은 객체 개념
print(a,type(a))
a = 'hello'
print(a,type(a))

# 동적 타이핑 = 변수에 새로운 값 할당 = 치환 = 정확히는 가르키는 주소의 변경

# 확장 치환문 ++ --와 같은 별도의 증감 연산자 없음 = a+=1로 표현
a = 1
print(a)
a += 10
print(a)

















