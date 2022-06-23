import re


datas = ['2022/08/08',
'1000/01/01',
'9999/12/313232322',
'900/02/02',
'12000/10/26',
'2021/13/01',
'2023/2/02',
'2024/06/3',
'2023/06/35',
]

regex = '^\d{4}\/(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[0-1])'

for data in datas :
    matchObj = re.match(regex,data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f'{data} {result}')



datas = [
'startcoding@maver.com',
'start-coding@maver.com',
'start_coding@maver.co.kr',
'startcoding@k-mail.com',
'@maver.com',
'startcoding?@k-mail.com',
'startcoding@k-mail',
'startcoding@maver',
]

regex = '^.([a-zA-Z0-9]|\_|\-){0,}@([a-zA-Z0-9\-]){0,}\.(\w{1,}|)(\.\w{1,})?'


for data in datas:
    matchObj = re.match(regex,data)
    result = (lambda x: True if x != None else False)(matchObj)
    print(f'{data} {result}')

