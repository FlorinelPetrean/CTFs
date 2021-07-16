    For this chall we got a binary which asks us for an address to write to and a value to put at the respective address. After decompiling with Ghidra we see that a certain "v" value is compared with 0x53585353. In Ghidra, we navigate to the address of "v" which is 0x00601058 and see that the value is 0x53535353. 
    Basically, what we need to do is to set the 3rd byte from right to left to 0x58. To point to that byte we need to add to "v" address +2 to set the pointer to exactly that byte. 
    We run the solve.py script and get a shell.
    We navigate to /home/ctf and use "cat flag" to get the flag.

    The flag is: SSS{aim_for_the_kill}
