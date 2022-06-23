import re




# 1. Group 그룹

str1 = '010-2343-3333'


# 1) 매칭되는 문자열 한개
result = re.match('\d{2,3}-\d{3,4}-(\d{4}$)',str1)
print(result.group(1)) # 그룹 1을 넘겨줌.


# 2) 매칭되는 문자열 여러개
str2 = '010-2343-7888,010-2343-1234,010-2343-5678,010-2343-9999,010-2343-2222'
result = re.finditer('\d{2,3}-\d{3,4}-(\d{4})(?=,|$)',str2)

for x in result:
    print(x.group(1))

# 3) substitution (교체)

str3 = '010-2343-3333'

result = re.sub('\d{4}$','****',str3)
print(result)
