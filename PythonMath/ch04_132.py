# 리스트는 추가,삭제,교체가 가능하지만 튜플은 요소 추가,삭제,교체가 불가능하다.
'''
sum = 0
i = 0
endNum = int(input("수 하나 입력 : "))
for i in range(1,endNum + 1):
    sum = sum + i
print("{}부터 {}까지 합 : {}".format(1,endNum,sum))
    
print(list(range(5)))

'''
'''

def add(a,b):
    c = a + b
    return c

def minus(a,b):
    d = a - b
    return d

def multiply(a,b):
    e = a * b
    return e

def divide(a,b):
    f = a / b
    return f

a = int(input("숫자1을 입력하시오 : "))
b = int(input("숫자2를 입력하시오 : "))

c = add(a,b)
d = minus(a,b)
e = multiply(a,b)
f = divide(a,b)

print("{}와 {}의 덧셈은{} 뺄셈은{} 곱셈은{} 나눗셈은{} 입니다.".format(a,b,c,d,e,f))

'''


def T_add(x,y):
    return x + y
def T_minus(x,y):
    return x + y
def T_multiply(x,y):
    return x + y
def T_divide(x,y):
    return x + y


while True :
    
    num1 = float(input("수1 입력 : "))
    op = input("연산자입력(+,-,*,/) : ")
    num2 = float(input("수2 입력 : "))

    if op == '+':
        print("{} + {} = {}".format(num1,num2,T_add(num1,num2)))
    elif op == '-':
        print("{} + {} = {}".format(num1,num2,T_minus(num1,num2)))
    elif op == '*':
        print("{} + {} = {}".format(num1,num2,T_multiply(num1,num2)))
    elif op == '/':
        print("{} + {} = {}".format(num1,num2,T_divide(num1,num2)))
    else:
        print("프로그램 종료")
        break;
    


    
    
    
'''
while 문 사용

i = 0
sum  = 0

while(i<100):
    i = i + 1
    sum+=i
print("sum =", sum)
'''
