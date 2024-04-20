
import numpy as np
import matplotlib.pyplot as plt

# 일변수 실함수
'''
a = 3
b = 2
x = np.linspace(1,5,30)
y = b ** x + a * x + b

plt.plot(x,y, 'bo-')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.show()
'''

# 이변수 실함수

'''
def f(x, y):
    return 3*x + 2*y

def f2(x,y):
    return 2*x**2 -3*x*y + 4*y**2

x = np.linspace(-3, 7, 100) # 배열로만들어짐
y = np.linspace(-3, 7, 100)
X, Y = np.meshgrid(x,y) # mesh는 그물을 의미함 meshgrid = 그물의 격자형태로 표시
Z = f2(X, Y)
fig =plt.figure() # 그림을 그릴 수 있는 새로운 창을 만든다. 기본적으로 빈 그림이 생성된다.
ax = fig.add_subplot(111, projection = '3d')
# ax = fig.gca(projection = '3d') 
ax.plot_surface(X, Y, Z, linewidth = 0.1)
#  init(elev,azim) = azim은 방위각(수평 각도)를 나타내며, 플롯을 좌우로 회전한다. 이렇게 하면 그래프의 시각적인 표현이 변경됨
ax.view_init(40, -100) # 양수 값은 플롯을 위로 올리고, 음수 값은 아래로 내린다 => 수직각도가 40도 수평각도가 -110도
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel('z')
plt.title("Surface Plot")

plt.show()
'''



# 일변수 벡터함수 그래프
'''

plt.figure(figsize = (7, 7))

ax = plt.axes(projection = '3d')
ax.xaxis.set_tick_params(labelsize = 15)
ax.yaxis.set_tick_params(labelsize = 15)

ax.set_xlabel('x', fontsize = 20)
ax.set_ylabel('y', fontsize = 20)

t = np.linspace(0, 2 , 101)
x = 2*t
y = t**2

ax.plot3D(x, y, c='k')
ax.plot([x[0]], [y[0]], 'o', markersize = 10, color = 'k', label = "t = {:.2f}".format(t[0]))
ax.plot([x[50]], [y[50]], '^', markersize = 10, color = 'k', label = "t = {:.2f}".format(t[50]))
ax.legend(fontsize = 15, loc="upper left")

plt.show()
'''

# 거듭제곱의 코드 구현
'''
def my_func (x):
    a = 4
    return x**a

x = np.linspace(1, 3)
y = my_func(x)

plt.plot(x, y)
plt.xlabel("x", size = 14)
plt.ylabel("y", size = 14)
plt.grid()

plt.show()
'''

# 제곱근의 코드구현

def my_func(x):
    return x ** (4/3) # x의 양의 제곱근. x ** (1/2)도 같음

x = np.linspace(0, 24)
y = my_func(x)  # y = f(x)

plt.plot(x, y)
plt.xlabel("x", size = 14)
plt.ylabel("y", size = 14)
plt.grid()

plt.show()
