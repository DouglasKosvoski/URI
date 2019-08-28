#include<stdio.h>

int main(){
  int cash;
  int a, b;

  scanf("%d", &cash);
  printf("%d\n", cash);

  a = cash / 100;
  printf("%d nota(s) de R$ 100,00\n", a);

  a = cash % 100;
  b = a / 50;
  printf("%d nota(s) de R$ 50,00\n", b);

  b = a % 50;
  a = b / 20;
  printf("%d nota(s) de R$ 20,00\n", a);

  a = b % 20;
  b = a / 10;
  printf("%d nota(s) de R$ 10,00\n", b);

  b = a % 10;
  a = b / 5;
  printf("%d nota(s) de R$ 5,00\n", a);

  a = b % 5;
  b = a / 2;
  printf("%d nota(s) de R$ 2,00\n", b);

  b = a % 2;
  a = b / 1;
  printf("%d nota(s) de R$ 1,00\n", a);
  return 0;
}
