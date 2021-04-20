from pwn import *

host = "34.107.72.222"
port = 31488

context.log_level = "CRITICAL"

def get_byte(start):
    end = start + 1
    r = remote(host,port)
    r.recvuntil(": ")
    r.sendline(str(start).encode())
    r.recvuntil(": ")
    r.sendline(str(end).encode())
    r.recvuntil(str(end).encode() + b'\r\n')
    byte = r.recvuntil("Enter")
    r.close()
    byte = byte[1 : -7]
    if byte == b'\r\n':
        return b'\n'
    elif len(byte) == 1:
        return byte
    else:
        return b'\x00'
    
    

i = 0
image = open("img", "wb+")
image.write(b'\x89')
while True:
    byte = get_byte(i + 1)
    image.write(byte)
    image.flush()
    i = i + 1
    print(byte)




