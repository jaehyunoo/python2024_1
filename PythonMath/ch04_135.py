import numpy as np

print(np.array([1,2,3]))

a = np.array([[0, 1],
             [3, 4]])

print(a + 3)
print()

print(a * 2)
print()

print(2 ** a)
print()

print(np.zeros(4)) # 1차원배열을 4열을 0으로 채워라.(실수꼴)
a = np.ones((2,3)) # 2행 3열에 해당하는 2차원 배열을 1로채워서 만들어라.(실수꼴)
print(a*5) # 연산된 결과가 나옴
print(np.shape(a)) # 배열의 모양을 나타냄 2행3열 => (2,3) 튜플의 형태로 나옴
print(len(a)) # 행의개수를 알 수 있음


print(np.arange(0,10)) # 0부터 9까지 1차원 배열에 다집어넣어라 (정수꼴)
print(np.linspace(0,10,5)) # 0에서 10 사이에 5개만 가져와서 만들어라.