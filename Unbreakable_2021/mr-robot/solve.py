from pwn import *

encoded_flag = "013032224029145C2047711D11562831021F077A1406782B28"
key = b'dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv'

flag = xor(bytes.fromhex(encoded_flag), key)
print(flag.decode())
