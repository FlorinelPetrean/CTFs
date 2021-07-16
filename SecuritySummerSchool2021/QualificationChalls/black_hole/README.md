
For this chall, we have a binary that seems to do nothing.
After decompiling using ghidra we see that the flag is redirected to /dev/null.
This means that at some point in the program, the flag is visible.
We open the binary in gdb and use the following commands:
catch syscall write

After this we can inspect the RSI register and there's the address of the flag and we get it:
SSS{the_more_you_look_the_less_you_actually_see}

Note: For this chall, pwngdb was used.
