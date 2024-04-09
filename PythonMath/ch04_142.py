import numpy as np

# 2차원 배열이 두개존재해야 3차원 배열이됨 인덱스는 3개 사용가능 [면][행][열]
a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])


print("합계 : ", np.sum(a))
print("평균 : ", np.average(a))

print("최대값 : ", np.max(a))
print("최소값 : ",np.min(a))
print("배열크기 : {} , 배열 차원 : {}".format(np.shape(a),a.ndim))
print("배열 행의 합 : {} \n 배열 열의 합 : {}".format(a.sum(axis=0),a.sum(axis=1))) 