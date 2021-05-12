from subprocess import *
from pwn import *

# for key in range(100):
key = 79 + 32
c_process = Popen(['./not_backdoor', str(key)], stdout=PIPE)
flag = c_process.stdout.readline()
print(flag)