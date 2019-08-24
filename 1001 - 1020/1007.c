#include<stdio.h>

int main(){
  int a,b,c,d;
  int result;

  scanf("%d%d%d%d\n", &a,&b,&c,&d);

  result = ((a*b) - (c*d));

  printf("DIFERENCA = %d\n", result);

  return 0;
}
