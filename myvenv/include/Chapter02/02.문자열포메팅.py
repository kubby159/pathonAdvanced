# 문자열 포메팅이 없다면?
# 기준님 수강기간이 7일 남았습니다.

name = '기준'
duration = '7'

message = name + '님 수강기간이 ' + duration +'일 남았습니다.'

print(message)

# 문자열 포메팅 사용 시 !

message_format = f'{name}님 수강기간이 {duration}일 남았습니다.'
print(message_format)