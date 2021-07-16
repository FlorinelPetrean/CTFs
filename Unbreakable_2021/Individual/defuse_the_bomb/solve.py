from pwn import *

elf = ELF("./defuse_kit")

p = elf.process()

true_code = [
    0x39, 0x30, 0x39, 
    0x34, 0x39, 0x32, 
    0x39, 0x52, 0x39, 
    0x34, 0x38, 0x53,
    0x30, 0x4e, 0x39,
    0x34, 0x30, 0x33,
    0x39, 0x34, 0x39,
    0x36, 0x39, 0x32,
    0x30, 0x37, 0x39,
    0x34, 0x00
]

code = "9094929R948S0N94039496920794"

p.recvuntil(":")

precalc_enc_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 10):
    char_nr = ord('0') + i
    result = (char_nr - 0x23) % 10
    precalc_enc_numbers[result] = chr(char_nr)


payload = "6761696E615F7A61706163697461"

for i in range(len(payload)):
    hex_chr = payload[i]

     
print(payload)

p.sendline(payload)

p.interactive()