    For this chall, we got what appears to be a windows executable file.
    We run the following command:
        file not_backdoor.exe 

    We observe that it is actually an archive. We can unarchive it with the following command:
        tar -x -f not_backdoor.exe

    We get an executable binary. We decompile it with Ghidra and see that the encrypted flag gets XORed with the parameter that we give as input. This means we have to choose a key which will decrypt our flag. 
    We run the solve.py script which will bruteforce the key and show all decrypted flags.
    To find the flag easier we can use grep the follwing way:
        python3 solve.py | grep SSS

    The flag is: SSS{pr3tty_c0nvoluted_fl4g}
    


    
    