#1. 위치 매개변수
# 가장 기본적인 매개변수

from turtle import title


def my_func(a,b):
    print(a,b)

my_func(2,3)


#2. 기본 매개변수
# 매개변수의 기본값을 지정할 수 있다.

def post_info(title,content='내용없음'):
    print('제목: ', title)
    print('내용: ', content)

post_info('출석합니다!')
#3. 키워드 매개변수
# 힘스 호출 시에 키워드를 붙여서 호출
# 매개변수의 순서를 지키지 않아도 됩니다.

def post_info(title,content):
    print("제목: ", title)
    print("내용: ", content)

post_info(content='내용없음', title= '여자친구 만드는 방법')
