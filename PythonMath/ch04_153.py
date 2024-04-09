# 심파이 : 기호 연산을 위한 오픈 소스 라이브러리
# 방정식을 풀때는 solve가 필요함
# 심파이가 취급하는 숫자에는 정수형(integer), 부동 소수점형(float), 분수형(rational)이 있다.
from sympy import*

x = symbols('x', integer = True)
print(x.is_integer)

y = symbols('y', postive = True)
print(sqrt(y**2))

print(cos(pi))
print(sin(pi))



x,y = symbols('x y')
f = Function('f') (x, y)

print(f.free_symbols)

k = Integer(5)

print(k)
print(type(k))

z = k / 3
print(z)
print(type(z))

print(Rational('1/3')) # Rational(1, 3)도 가능
print(Rational(2, 6))

# 2x ** 3 + 5x -4의 수식 표현

# 수식대체 subs()


# 정수를 포함한 같은 수식 evalf() 함수
eq = pi /2
print(eq)
print(eq.evalf(5)) # 소수점 기본적으로는 15자리 지정하려면 eq.evalf(원하는 소숫자리 개수)
print(N(eq,5)) # 위와 동일한 형태