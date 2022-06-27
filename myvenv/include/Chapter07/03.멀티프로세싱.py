import multiprocessing as mp


# 프로세스에서 실행할 함수

def sub_process(name):
    print('[sub] start')
    print(name)
    cp = mp.current_process()
    print(f'[main] pid : {cp.pid}') # pid : 프로세스의 아이디
    print('[sub] end')



# 메인 프로세스
# main 모듈일때만 실행한다.
if __name__ == "__main__":
    print('[main] start')
    p =  mp.Process(target=sub_process, args=('startcoding',))
    p.start()
    cp = mp.current_process()
    print(f'[main] pid : {cp.pid}') # pid : 프로세스의 아이디
    print('[main] end')


