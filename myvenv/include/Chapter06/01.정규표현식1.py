import re


# 1. re 모듈의 메서드

str = 'love people around you, love your workd, love yourself'

# 1) match : 문자열의 처음부터 검색( 결과는 1개의 match 객체)

result = re.match('love',str)
print(result)

# 2) search : 문자열의 전체를 검색( 결과 : 1 개의 match 객체)

result = re.search('people',str)
print(result)


# 3) findall : 문자열의 전체를 검색(결과 : 문자열 리스트)

result = re.findall('love',str)
print(result)


# 4) finditer : 문자열의 전체를 검색 (결과 : match 객체 이터레이터)

result = re.finditer('love',str)
print(result)


for x in result:
    print(x)


# 5) fullmatch 패턴과 문자열이 완벽하게 일치하는 지 검사
str2 = 'Hey Guys, read books'
result = re.fullmatch('.*',str2)
print(result)


# 2. match object의 메서드

result = re.search('people',str)

# 1) group() : 매칭된 문자열을 반환
print(result.group())

# 2) start() : 매칭된 문자열의 시작 위치 반환
print(result.start())

# 3) end() : 매칭된 문자열의 끝 위치 반환
print(result.end())

# 4) span() : 매칭된 문자열의 (시작, 끝) 위치 튜플을 반환
print(result.span())