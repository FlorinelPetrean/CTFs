from pwn import *

IP = "35.198.90.23"
port = 30147

p = remote(IP, port)

p.recvuntil("What does the S in RSA stand for?")
p.sendline("shamir")

p.recvuntil("If p is 19 and q is 3739, what is the value of n?")
p.sendline(str(19 * 3739))

p.recvuntil("That was too simple! If n is 675663679375703 and q is 29523773, what is the value of p?")
number = int(675663679375703 / 29523773)
print(number)
p.sendline(str(number))

p.recvuntil("Ok, I'll just give you something harder!\nn=616571, e=3, plaintext=1337")

ciphertext = "62587 75907"

print(ciphertext)

p.sendline(ciphertext)





p.interactive()