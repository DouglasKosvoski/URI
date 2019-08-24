#include<stdio.h>

int main(){
  int code;
  int units;
  double unit_price;
  double total = 0;

  int i=0;
  while(i<2){
    scanf("%d %d %le\n", &code, &units, &unit_price);
    total += (units * unit_price);
    i++;
  }

  printf("VALOR A PAGAR: R$ %.2f\n", total);
  return 0;
}
