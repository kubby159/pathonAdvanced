# 1. 이터러블 객체(iterable object)
# 문자열, 리스트, 튜플, 딕셔너리, range 객체


# for i in '123':
# print(i)





iter_obj = ([1,2,3].__iter__())

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())