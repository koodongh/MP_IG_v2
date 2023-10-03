import fcntl
import sys
import os

lock_file_path = "/home/user/cam/share/Python/send.py"

def is_script_running(lock_file_path):
    lock_file = open(lock_file_path, 'w+')
    try:
        fcntl.lockf(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return False
    except IOError:
        return True

if is_script_running(lock_file_path):
    print("The script is already running.")
    sys.exit(1)

# Your main script logic here...
