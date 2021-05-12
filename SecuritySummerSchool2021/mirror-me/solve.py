from pwn import *


IP = "141.85.224.99"
port = 31338

p = remote(IP, port)

p.recvuntil("Insert the corect numbers in order to get the flag\n")
p.sendline("993")
p.sendline("913")
p.interactive()