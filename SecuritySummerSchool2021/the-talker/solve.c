#include <stdio.h> // standard input and output library
#include <stdlib.h> // this includes functions regarding memory allocation
#include <string.h> // contains string functions
#include <errno.h> //It defines macros for reporting and retrieving error conditions through error codes
#include <time.h> //contains various functions for manipulating date and time
#include <unistd.h> //contains various constants
#include <sys/types.h> //contains a number of basic derived types that should be used whenever appropriate
#include <arpa/inet.h> // defines in_addr structure
#include <sys/socket.h> // for socket creation
#include <netinet/in.h> //contains constants and structures needed for internet domain addresses


int main(){
    int sock = 0, valread;
    struct sockaddr_in serv_addr;
    char buffer[1024] = {0};
    if ((sock = socket(0x2, 0x2, 0x11)) < 0)
    {
        printf("\n Socket creation error \n");
        return -1;
    }
    memset((void*)&serv_addr, 0, 0x10);
   
    serv_addr.sin_family = 0x2;
    serv_addr.sin_port = htons(0x115c); // port 4444
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY); 

   
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        printf("\nConnection Failed \n");
        return -1;
    }
    valread = read( sock , buffer, 0x80);
    printf("%s\n",buffer );
    return 0;
}