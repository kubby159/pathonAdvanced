def print_fruits(*args):
    for arg in args:
        print(arg)


print_fruits('apple','orange','mango','grape')


def comment_info(**kwargs):
    print(kwargs) # {'name': '파린이', 'content': '정말 감사합니다.'}
    # for key,value in kwargs.items():
    #     print(f'{key}:{value}')

comment_info(name='파린이',content='정말 감사합니다.')


# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드 (기본) - 키워드 가변