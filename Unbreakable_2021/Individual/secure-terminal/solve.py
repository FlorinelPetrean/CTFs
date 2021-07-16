from pwn import *

IP = "35.234.117.20"
port = 30361

p = remote(IP, port)


