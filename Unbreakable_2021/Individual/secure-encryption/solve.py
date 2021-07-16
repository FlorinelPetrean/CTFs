from pwn import *

IP = "35.198.90.23"
port = 31200

p = remote(IP, port)

p.recvuntil("ENC= b'")

enc_flag = p.recvuntil("'\nValue:")

print(enc_flag)


p.interactive()


