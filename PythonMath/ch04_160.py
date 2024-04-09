import numpy as np
from sympy import*

# x,y,z = symbols('x y z')
x = symbols('x')
y = symbols('y')
z = symbols('z')
print((x + y).subs({x : z**2, y : sqrt(z)}))


eq = pi / 2
print(eq)
print(eq.evalf()) # evalf() 함수를 호출하면 수식이 계산되고 심파이의 부동 소수점 결과를 반환한다.

print(solveset(x**2 - 2*x + 1)) # solveset() 함수를 사용하여 방정식의 해를 구할 수 있다.

expr = Eq(x ** 2 + 2*x +1, 0) # 
print(solveset(expr))

print(factor(expr)) # factor은 인수분해를 해준다.


print(solveset(x**2 - 2*x +1))   # x**2 - 2x + 1 = 0
print(solveset(Eq(x**2,2*x-1)))  # x**2 = 2x -1   => x**2 -2x +1 = 0


eq1 = x + y - 7
eq2 = -3 * x - y + 5
print(linsolve([eq1,eq2],[x,y])) # 연립 방정식은 linsolve()[선형] 함수와 nonlinsolve()[비선형]함수를 사용

eq3 = x * y -1
eq4 = x - 2
print(nonlinsolve([eq3, eq4], [x,y]))

# simplify() 함수는 수식을 간단하게 만들 수 있음
print(simplify(cos(x)**2 + sin(x)**2))

expr1 = x**2 + 5*x + 3*(x-1) + (x-1)**2
print(simplify(expr1))  # 식을 풀어서 단순화시켜준다
print(solveset(expr1))  # 방정식의 해 구하기.

print(expand((x-1)*(x-2)))  #  expand함수는 수식을 전개해준다
print(factor(x ** 3 - 8)) # factor함수는 수식을 인수분해 해준다.

expr2 = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
print(collect(expr2,x)) # collect함수는 수식을 특정 변수의 다항식으로 정리한다.

expr3 = (x**2 + 2*x + 1) / (x**2 + x)
print(cancel(expr3)) # cancel 함수는 분수의 분자와 분모를 약분하여 간단한 형태로 만든다.