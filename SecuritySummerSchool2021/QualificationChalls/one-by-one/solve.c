#include <stdio.h>

int main(){
    char flag[30];
    flag[20] = 0x64; 
    flag[0] = 0x53 ;
    flag[24] =  0x6f; 
    flag[18] = 0x6f ;
    flag[3] = 0x7b ;
    flag[27] = 0x7d ;
    flag[11] = 0x6f ;
    flag[13] = 0x5f ;
    flag[23] = 0x6c ;
    flag[12] = 0x66 ;
    flag[14] = 0x74 ;
    flag[21] = 0x5f ;
    flag[9] = 0x70 ;
    flag[26] = 0x6b ;
    flag[17] = 0x5f ;
    flag[25] = 0x63 ;
    flag[15] = 0x68 ;
    flag[6] = 0x63 ;
    flag[7] = 0x68 ;
    flag[22] = 0x62 ;
    flag[2] = 0x53 ;
    flag[8] = 0x69 ;
    flag[5] = 0x5f ;
    flag[19] = 0x6c ;
    flag[4] = 0x61 ;
    flag[16] = 0x65 ;
    flag[1] = 0x53 ;
    flag[10] = 0x5f;

    printf(flag);
}