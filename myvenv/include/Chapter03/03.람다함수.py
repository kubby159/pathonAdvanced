
# 기존 함수 정의 방법
def minus_one(a):
    return a-1


#lambda 매개변수:결과
lambda a: a-1


#기존 함수 호출 방법
minus_one(10)

#lambda 함수 호출 방법
#1.(lambda a: a-1)(10)
#2.plus_one = lambda a:a+1, plus_one(10)


#기존 함수에서 if 문 사용

# def is_positive_number(a):
#     if a>0:
#         return True
#     else:
#         return False

#람다함수 정의방법(람다에서 조건문 사용 시 else까지 꼭 써줘야한다.)
lambda a:True if a>0 else False
print((lambda a:True if a>0 else False)(-2)) #False
is_positive_number = lambda a:True if a>0 else False
print(is_positive_number(2)) #True
