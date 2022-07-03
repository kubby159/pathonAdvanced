# 메모리 사용을 효율적으로 하기 위해서 사용한다.

import sys


list_data = [i*3 for i in range(1,10000+1)]
generator_data =(i*3 for i in range(1,10000+1))


print(sys.getsizeof(list_data))