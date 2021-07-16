#!/usr/bin/env python3

from pwn import *

IP = "35.246.187.27"
port = 30684

exe = ELF("./the_matrix")
libc = ELF("./libc-2.27.so")
ld = ELF("./ld-2.27.so")

context.binary = exe
context.terminal = ["terminator", "-e"]


def conn():
    if args.LOCAL:
        return process([ld.path, exe.path], env={"LD_PRELOAD": libc.path})
    else:
        return remote(IP, port)


def main():
    r = conn()

    gdb.attach(r, gdbscript='''b main''')

    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
