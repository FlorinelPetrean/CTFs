from pwn import *

stuff = b"\xb0\x8a\x91\x96\x81\xb6\x97\x86\x88\xb0\xc3\x9d\x94\x81\xc7\x87\x80\xac\x8a\xc3\x86\xac\x95\xc3\x86\x9d\x97\xac\xc2\x87\x8e"
key = 0xf3
flag = "".join(chr(byte ^ key) for byte in stuff)

print(flag)