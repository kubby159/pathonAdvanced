from ast import keyword
import threading

# 스레드에서 실행할 함수

def work():
    print('[sub] start')
    keyword = input('[sub] 검색어를 입력하세요.>>>')
    print(f'[sub] {keyword}로 검색을 시작합니다...')
    print('[sub] end')




# 메인스레드 실행되는 부분
print('[main] start')

worker = threading.Thread(target=work)
worker.daemon = True #daemon 속성을 이용해서 메인스레드 종료 시 서브스레드도 같이 종료하게 만들 수 있음.
worker.start()

print('[main] 메인 스레드는 자기할일을 합니다..')
print('[main] end')