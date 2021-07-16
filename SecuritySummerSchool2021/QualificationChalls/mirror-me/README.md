    For this chall we have a binary which asks us for 2 numbers in order to get a shell of the host.
    after decompiling with Ghidra we see that the product of those 2 numbers is getting checked with a value returned from the function max_mirror().

    In order to get this value, I wrote the max_mirror.c which mimics the max_mirror() function of the binary. We compile it and run it and we get the following:
        i = 995
        j = 583
        i = 993
        j = 913
    We choose the last i and j. The product of i*j will be compared with our input when running the binary. Of course, this value could have been also discovered with gdb and choose i = 1 and j = number that we discovered.
    We run the solve.py python script in order to send i and j to the binary and the shell.
    We navigate to home/ctf and "cat flag". 

    The flag is: SSS{Mirror_mirror_on_the_wall_who_is_the_fairest_of_them_all}
