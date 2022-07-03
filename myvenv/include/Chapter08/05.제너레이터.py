# 제너레이터


# 1. 이터레이터를 만드는 함수

def season_generator(*args):
    for arg in args:
        yield arg # yield : 리턴하고 난 후 잠시 지연시킨다.


g = season_generator('spring','summer','autumn','winter')
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


def func():
    print('첫번째 작업 중...')
    yield 1

    print("두번째 작업 중...")
    yield 2

    print('세번째 작업 중...')
    yield 3

# return 은 반환 값을 뱉고 나서 바로 실행을 종료시켜버리지만, yield 는 리턴값을 반환하하고, 다음 작업을 계속해서 진행해나간다. 

ge = func()
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)