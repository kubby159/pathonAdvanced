#1. map 함수
# - 사용 이유
# 기존 리스트를 수정해서 새로운 리스트를 만들 때 

# - 사용방법
# map(함수, 순서가 있는 자료형)
print(list(map(int,['3','4','5'])))



# - 예제
# 리스트 모든 요소의 공백제거

# 1) for문 사용
items = ['    로지덱마우스','    앱솔키보드    ']

for x in range(len(items)):
    items[x] = items[x].strip()


print(items)

# 2) map 사용

def test(x):
   return x.strip()

print(list(map(test,items)))


# 3) 람다함수 사용
items = list(map(lambda a: a.strip(), items))
print(items)


# 2. filter 함수
# - 사용이유
# 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때

# - 사용 방법
# filter(함수, 순서가 있는 자료형)
def func(x):
    return x < 0


print(list(filter(func,[-3,-2,0,5,7])))

# - 예제
# 리스트에서 길이가 3이하인 문자들만 필터링
animals = ['cat','tiger','dog','bird','monkey']

# 1) for 사용
result = []
for word in animals:
    if len(word) <= 3:
        result.append(word)


print(result)


# 2) filter 사용
def filter_word(x):
    return len(x) <= 3

print(list(filter(filter_word,animals)))

# 3) 람다 함수 사용
print(list(filter(lambda a : len(a) <= 3,animals)))