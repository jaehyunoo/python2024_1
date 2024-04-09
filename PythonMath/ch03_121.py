import math # math 모듈 가져오기

print("인공지능 수학")

a = 7
b = 4


print("덧셈 :", a + b)

print("뺄셈 :", a - b)

print("곱셈 :", a * b)

print("나눗셈(소수점 이하 버리지 않음) :", a / b)

print("나눗셈(소수점 이하 버림, 정수) :", a // b)

print("나머지 연산 :", a % b)

print("거듭제곱 :", a ** b)


print("2의 제곱근 = ", math.sqrt(3))
print("3의 지수함수 = ", math.exp(10))
print("5의 자연로그값 = ", math.log(1))
print("파이의 코사인값 = ", math.cos(math.pi * -2))
print("파이의 사인값 = ", math.sin(math.pi / 6))
print("파이의 탄젠트값 = ", math.tan(math.pi / -4))

d = [[11, 22, 33], [44, 55, 66]]
print(d)
print(d[1])
print(d[0][2])
print(d[1][2])
