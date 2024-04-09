import numpy as np
import matplotlib.pyplot as plt

a = int(input("상수를 입력하시오 : "))  # a는 상수
x = np.linspace(0,5)    # x는 1부터 5까지 범위를 갖는 변수
y = a * x       # y는 변수
y2 = a * x + 3 

plt.plot(x,y,"r^")
plt.plot(x,y2,"b^")
plt.xlabel("x", size = 15)
plt.ylabel("y", size = 15)
plt.grid()

plt.show()