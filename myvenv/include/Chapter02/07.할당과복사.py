# 리스트 할당 방식
import copy
x = [1,2,3,4,5]
y = x

y[2] = 0
print(x)
print(y)
print(id(x)) # 주소 값 찾기.
print(id(y))

# 리스트 복사 방식
x = [1,2,3,4,5]
y = x.copy()
y[2] = 0

print(x) # [1, 2, 3, 4, 5]
print(y) # [1, 2, 0, 4, 5]


# 다차원 리스트 복사 방식
x = [[1,2],[3,4,5]]
y = copy.deepcopy(x)
