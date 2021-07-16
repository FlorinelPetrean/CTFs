#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* encrypt(char *input){
  size_t len_input;
  void *output;
  int local_20;
  int i;
  
  len_input = strlen(input);
  output = (char*)malloc(len_input * sizeof(char));
  i = 0;
  while(1) {
    len_input = strlen(input);
    if (len_input <= (long)i) break;
    if ((input[i] < 'A') || ('Z' < input[i])) {
      if ((input[i] < 'a') || ('z' < input[i])) {
        if ((input[i] < '0') || ('9' < input[i])) {
          *(char *)((long)output + (long)i) = input[i];
        }
        else {
          *(char *)((long)output + (long)i) =
               (char)(input[i] + -0x23) + (char)((input[i] + -0x23) / 10) * -10 + '0';
        }
      }
      else {
        local_20 = input[i] + 0xd;
        if (0x7a < local_20) {
          local_20 = input[i] + -0xd;
        }
        *(char *)((long)output + (long)i) = (char)local_20;
      }
    }
    else {
      *(char *)((long)output + (long)i) = input[i] + '\r';
      if ('Z' < *(char *)((long)output + (long)i)) {
        *(char *)((long)output + (long)i) = *(char *)((long)output + (long)i) + -0x1a;
      }
    }
    i = i + 1;
  }
  return output;
}

int main(){
    char enc_code[] = "9094929R948S0N94039496920794";
    char enc_code1[] = {
        0x39, 0x30, 0x39, 
        0x34, 0x39, 0x32, 
        0x39, 0x52, 0x39, 
        0x34, 0x38, 0x53,
        0x30, 0x4e, 0x39,
        0x34, 0x30, 0x33,
        0x39, 0x34, 0x39,
        0x36, 0x39, 0x32,
        0x30, 0x37, 0x39,
        0x34, 0x00
    };
    char code[29];

    int precalc_numbers[10];
    for(int i = 0; i < 10; i++){
        char char_nr = '0' + i;
        char aux = (char_nr - 0x23) - ((char_nr - 0x23)/10) * 10 + '0'; // = (char_nr - 0x23) % 10
        int result = aux - '0';
        precalc_numbers[result] = char_nr;
    }


    int precalc_lowercase_chars[26];
    for(int i = 0; i < 26; i++){
        char char_nr = 'a' + i;
        char aux = char_nr + 0xd;
        if(aux > 'z')
            aux = char_nr - 0xd;
        int result = aux - 'a';    
        precalc_lowercase_chars[result] = char_nr;
    }

    int precalc_uppercase_chars[26];
    for(int i = 0; i < 26; i++){
        char char_nr = 'A' + i;
        char aux = char_nr + 0xd;
        if(aux > 'Z')
            aux = aux - 0x1a;
        int result = aux - 'A';    
        precalc_uppercase_chars[result] = char_nr;
    }


    for(int i = 0; i < strlen(enc_code); i++){
        char c = enc_code[i];
        char new_c = 0;
        if (c >= '0' && c <= '9'){
            int nr = c - '0';
            new_c = precalc_numbers[nr];
        }
        else if (c >= 'a' && c <= 'z'){
            int nr = c - 'a';
            new_c = precalc_lowercase_chars[nr];
        }
        else if (c >= 'A' && c <= 'Z'){
            int nr = c - 'A';
            new_c = precalc_uppercase_chars[nr];
        }
        else{
            new_c = c;
        }
        code[i] = new_c;

    }
    code[29] = 0x00;
    printf("%s\n", code);

    for(int i = 0; i < strlen(code); i++){
      printf("%x", code[i]);
    }

    printf("\n");


    char* test = encrypt(code);

    printf("test = %s\n", test);





}