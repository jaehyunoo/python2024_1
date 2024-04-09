
import numpy as np
import matplotlib.pyplot as plt
from random import randint # random중에서 randint만 가져오는 것것

# 한글사용을 위한 명령(5,6 line)
plt.rcParams['font.family'] ="Malgun Gothic"#macos #"Malgun Gothic" window
plt.rcParams['axes.unicode_minus'] =False

x = np.array([1,2,3,4,5,6,7])
y = np.array([78.8,78.4,78.7,78.5,78.4,79.2,78.6])

z = np.linspace(-5,5, 300) # np.linspace(시작값,마지막값, 샘플개수) 개수를 안넣을경우 50개가 나온다.

# plt.plot(x, y, color = "r", marker = "o") # color = "r", marker="o" 와 동일.
# plt.grid() # 그리드(격자) 형식으로 나타낸다.

k1 = z ** 2
k2 = (z - 2) ** 2
# plt.plot(z, k1, color = "r") # 선은 빨간색
# plt.plot(z, k2, color = "k", linestyle = ":") # 색은 검정색, "--"하면 점선, "-"은 실선, "-."은 대쉬닷, ":" 닷라인

# 축 레이블
plt.xlabel("X축", size = 14)
plt.ylabel("Y축", size = 14)

# 범례 및 선 스타일 지정
plt.plot(z, k1, label = "y1 value", color = "r") # 빨간 색 지정
plt.plot(z, k2, label = "y2 value", linestyle = ":", color ="k") # 선스타일과 색상 지정

# 범례 표시
plt.legend()

plt.title("공업수학")
plt.grid()
plt.show()


# 히스토그램 그리기.

data = np.array([60,71,62,62,62,62,71,65,68,65,66,66,67,67,68,68,68,69,60,71])
plt.title("히스토그램 그리기")
plt.hist(data, bins = 20, histtype = 'bar') # bins = 구간의 수 (기본값은 10)
# hisstype  
# bar : 전통적인 막대형태 히스토그램, barstackted : 여러 데이터가 쌓인 막대 형태, step : 내부가 비어있는 lineplot 형태 stepfilled : 내부가 차있는 linplot 형태
plt.show()