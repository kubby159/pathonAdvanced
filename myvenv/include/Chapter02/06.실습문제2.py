words_list = ['오메가3',None,'비타민C500',None,"홍상절편"]


# 리스트 내포 미사용
result = []
for word in words_list:
    if word == None:
       result.append("")
    else:
        result.append(word)

print(result)


# 리스트 내포 사용 시
# words = ["" if i == None else i for i in words_list]
# print(words)