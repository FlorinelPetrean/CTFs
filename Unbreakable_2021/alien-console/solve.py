
from pwn import *
import string
host = "34.89.213.64"
port = 32547

context.log_level = "CRITICAL"
alphabet = "0123456789abcdef}"

initial_flag = "ctf{"
def decrypt(flag):
    while flag[-1] != "}":
        for p in alphabet:
            r = remote(host, port)
            r.recvuntil(": ")
            aux = flag
            aux = aux + p
            print(aux)
            r.sendline(aux)
            r.recvuntil(aux.encode() + b'\r\n')
            encoded_flag = r.recvuntil(b'\r\n')[:-2].decode()
            test = "00" * len(aux)
            print(test)
            print(encoded_flag[:len(test)])
            if encoded_flag[:len(test)] == test:
                flag = flag + p 
    return flag


flag = decrypt(initial_flag)
print(flag)

found_flag = "ctf{5b838db4a213b1e2c001bef7192712c5d2b69a69fe116e3b6b06ba5fa6555da0}"




