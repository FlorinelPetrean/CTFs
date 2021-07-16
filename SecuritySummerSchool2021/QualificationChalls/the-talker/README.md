    For this chall we get a binary called "the-talker". We analyze it with Ghidra and see that it creates a socket on the host on port 4444 will send the flag to that socket. Also, the socket uses the UDP connection.
    We ssh to the remote server with the give credentials and we have to find a way to listen on the 4444 port. We can do this using netcat.
    We run the command: nc -lvu -p 4444.
    We wait a little bit and see the flag written on the screen.

    The flag is: SSS{the_talker_has_spoken}