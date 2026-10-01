import numpy ad np # Thiry party. 별도 설치 필요

# numpy 배열 생성
np_array = np.array([3, '2', 1.7]) # 이질적인 원소들
print(np_array, type(np_array)) # 한 가지 타입(상위 타입)으로 변환됨

# python 리스트 생성
list_array = [3, '2', 1.7] # 이질적인 원소들
print(list_array, type(list_array) # 그대로 출력, 속도는 단점


import array

a = array.array[float | int] ( typecode: 'f', initializer:(1.0, 1.5, 2.0, 2.5))
print(a)
print(a[1])
# a[1] = "1" # TypeError: must be real number, not str
a[1] = -9.12
print(a) # array('f', [1.0, -9.119999885559082, 2.0, 2.5]), IEEE754 부동소수점