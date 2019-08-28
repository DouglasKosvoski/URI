#include<stdio.h>

int main(){
  int years, months, days;
  int age;

  scanf("%d", &age);

  years  = age / 365;
  months = age % 365 / 30;
  days   = age % 365 % 30;

  printf("%d ano(s)\n", years);
  printf("%d mes(es)\n", months);
  printf("%d dia(s)\n", days);
  return 0;
}
