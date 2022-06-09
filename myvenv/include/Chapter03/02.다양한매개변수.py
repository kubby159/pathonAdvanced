def print_fruits(*args):
    for arg in args:
        print(arg)


print_fruits('apple','orange','mango','grape')


def comment_info(**kwargs):
    print(kwargs) # {'name': '파린이', 'content': '정말 감사합니다.'}
    # for key,value in kwargs.items():
    #     print(f'{key}:{value}')

comment_info(name='파린이',content='정말 감사합니다.')
