from pwn import *


binary = ELF("./crypto_crackme")
p = binary.process()

pass_enc_file = open("secret.enc")
secret = pass_enc_file.read()

indexes_string = "0 7 14 1 8 15 2 9 16 3 10 17 4 11 18 5 12 19 6 13"
indexes = []
for x in indexes_string.split(" "):
    print(int(x))
    indexes.append(int(x))


password = ""
for i in indexes:
    password = password + secret[i]

p.recvuntil("What is the secret password?\n")
p.sendline(password)
p.interactive()

