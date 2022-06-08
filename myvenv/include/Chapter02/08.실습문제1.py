time = input('소요시간입력>>> ')

hours = 0
minute = 0

for x in time:
    if x =='시':
        hour_index = time.index(x)
        hours = int(time[:hour_index])
        hours *= 60
   

    if x == '분':
        minutes_index = time.index(x)
        minute = int(time[minutes_index-2:minutes_index])
        
result = hours+minute

print(result)