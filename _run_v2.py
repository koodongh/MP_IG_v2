import os
import time

def run_1():
    process_read = os.popen("ps -ef | grep main.py | grep -v 'grep'").readlines()
    # ps -ef 명령어를 이용해서 현재 프로세스를 출력한 후, 그 중 run24h.py 문자열이 포함된 줄만 모은다.
    # grep 명령어 자체도 프로세스에 나타나므로 grep -v를 이용해서 제외한다.
    check_process = str(process_read)
    # 문자열로 변환한다.
    text_location=check_process.find("main.py")

    if ( text_location == -1 ):
        print("Process not found!")
        path = '/home/user/cam/share/Python'
        os.chdir(path)
        os.system("sudo nohup python3 /home/user/cam/share/Python/main.py &")
        # 해당 프로그램을 다시 실행한다. 백그라운드에서 실행할 경우 &기호를 붙인다.
        print("Program restarted!")
    else:
        print("Process exists. Location is",text_location)

def run_2():
    process_read = os.popen("ps -ef | grep send.py | grep -v 'grep'").readlines()
    # ps -ef 명령어를 이용해서 현재 프로세스를 출력한 후, 그 중 run24h.py 문자열이 포함된 줄만 모은다.
    # grep 명령어 자체도 프로세스에 나타나므로 grep -v를 이용해서 제외한다.
    check_process = str(process_read)
    # 문자열로 변환한다.
    text_location=check_process.find("send.py")

    if ( text_location == -1 ):
        print("Process not found!")
        os.system("sudo nohup python3 /home/user/cam/share/Python/send.py &")
        # 해당 프로그램을 다시 실행한다. 백그라운드에서 실행할 경우 &기호를 붙인다.
        print("Program restarted!")
    else:
        print("Process exists. Location is",text_location)

if __name__ == "__main__":
    while True:
        run_1()
        time.sleep(1)
        run_2()
        time.sleep(20)
    
