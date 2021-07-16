    For this chall we get a binary which seems to just print Hello World to the screen.
    We run "strings one_by_one" and see that we have a lot of strings with format "part{nr}", which could be parts of our flag.

    We will disassemble the binary with Ghidra and search the "part" string in the Program Text. We discover a section in the binary with all the parts of the flag. All we have to do now is to put them in order.
    By compiling solve.c and running the "solve" binary we get the flag.

    The flag is: SSS{a_chip_of_the_old_block}