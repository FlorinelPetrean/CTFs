from subprocess import *
from pwn import *

for key in range(200):
    # key = 111
    c_process = Popen(['./not_backdoor', str(key)], stdout=PIPE)
    flag = c_process.stdout.readline()
    print(flag)