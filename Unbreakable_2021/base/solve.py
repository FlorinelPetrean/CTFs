from pwn import *
import sys
from string import *

IP = "35.198.90.23"
port = 30789

p = remote(IP, port)

p.recvuntil("What is the value of <<")
number = p.recvuntil(">>")
print(number[:-2])
hex_value = hex(int(number[:-2]))
print(f"hex number: {hex_value}\n")
p.recvuntil("Input: ")
p.sendline(str(hex_value))



p.recvuntil("What is the value of <<")
string = p.recvuntil(">>")[:-2]
print(string)
string_value = ""
for i in range(0, len(string), 2):
    ascii_aux = string[i:i+2]
    number = int(ascii_aux, base=16)
    char = chr(number)
    string_value = string_value + char
print(string_value)
p.recvuntil("\n")
p.recvuntil("Input:")
p.sendline(string_value)


p.recvuntil("What is the value of <<")
another_string = p.recvuntil(">>")[:-2]
print(another_string)
another_string_value = ""
for i in range(0, len(another_string), 5):
    ascii_aux = another_string[i:i+4]
    number = int(ascii_aux, base=8)
    char = chr(number)
    another_string_value = another_string_value + char
print(another_string_value)
p.recvuntil("\n")
p.recvuntil("Input:")
p.sendline(another_string_value)


flag = str(p.recv())
print(flag)
p.interactive()
    
