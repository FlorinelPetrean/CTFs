#include <stdio.h>

void decrypt_flag(int key){
    char xor_flag[28];
    char flag[28];

    xor_flag[0] = 0x3c;
    xor_flag[1] = 0x3c;
    xor_flag[2] = 0x3c;
    xor_flag[3] = 0x14;
    xor_flag[4] = 0x1f;
    xor_flag[5] = 0x1d;
    xor_flag[6] = 0x5c;
    xor_flag[7] = 0x1b;
    xor_flag[8] = 0x1b;
    xor_flag[9] = 0x16;
    xor_flag[10] = 0x30;
    xor_flag[11] = 0xc;
    xor_flag[12] = 0x5f;
    xor_flag[13] = 1;
    xor_flag[14] = 0x19;
    xor_flag[15] = 0;
    xor_flag[16] = 3;
    xor_flag[17] = 0x1a;
    xor_flag[18] = 0x1b;
    xor_flag[19] = 10;
    xor_flag[20] = 0xb;
    xor_flag[21] = 0x30;
    xor_flag[22] = 9;
    xor_flag[23] = 3;
    xor_flag[24] = 0x5b;
    xor_flag[25] = 8;
    xor_flag[26] = 0x12;
    xor_flag[27] = 0x6f;
    xor_flag[28] = '\n';

    for(int i = 0; i < 29; i++){
        flag[i] = xor_flag[i] ^ key;
    }
    printf("flag = %s\n", flag);

}

int find_key() {
    char ch = 0x3c;
    char key;
    char S = 0x53;
    for(char i = 0; i < 100; i++){
        if(i ^ ch == S) {
            key = i;
            break;
        }
    }
    printf("key = %d\n", (int)key);
    return key;
}


int main(){
    int key = find_key();

    decrypt_flag(key);
}