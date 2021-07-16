from os import truncate
from pwn import *



file = open("mastermind.bin", mode="r")

string = file.read()

file.close()

string = string.replace('\n', '')
# string = string.replace('ff', '00')
# string = string.replace('fe', '00')
# string = string.replace('8d', '00')
string = string.replace(' ', '')
string = string.replace("\\x", "")


bytes = bytearray.fromhex(string)

print(bytes)

# asm_instr = disasm(bytes)
# print(asm_instr)


p = run_shellcode(bytes)
p.wait_for_close()
p.poll()
# gdb.attach(p)
# p.interactive()


