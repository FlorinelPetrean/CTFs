#include <stdio.h>

int check_cond(long number)
{
  long a;
  long b;
  
  b = 0;
  a = number;
  while (a != 0) {
    b = a % 10 + b * 10;
    a = a / 10;
  }
  return b == number;
}

int max_mirror(void)

{
  int prod;
  int is_mirror;
  int i;
  int j;
  int max_nr;
  
  max_nr = 0;
  i = 999;
  while (100 < i) {
    j = i;
    while (100 < j) {
      prod = j * i;
      is_mirror = check_cond(prod);
      if ((is_mirror != 0) && (max_nr < prod)) {
        printf("i = %d\n", i);
        printf("j = %d\n", j);
        max_nr = prod;
      }
      j = j - 1;
    }
    i = i - 1;
  }
  return max_nr;
}

int main(){
    max_mirror();
}