# 리스트 메서드

# 리스트 데이터 삭제
fruits = ['apple','orange', 'mango']
del fruits[1]
print(fruits) # ['apple', 'mango']


# 리스트 정렬
# -오름차순
numbers = [7,5,1,2,8,3]
numbers.sort()
print(numbers)

# -내림차순
numbers.sort(reverse=True)
print(numbers)

# enumerate

titles = ['출석!!','출석인증합니다!','출석이요!!']

for index, title in enumerate(titles, 1): # 두 번째 인자로 시작번호 설정가능하다.
    print(f'{index}번 째 글입니다. 제목 : {title}')
# 0 출석!!
# 1 출석인증합니다!
# 2 출석이요!!