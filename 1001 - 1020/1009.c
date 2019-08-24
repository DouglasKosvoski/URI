#include<stdio.h>

int main(){
  char name;
  double salary;
  double sales;
  double total;

  scanf("%s %le %le\n", &name,&salary,&sales);

  total = (salary + (sales * 0.15));

  printf("TOTAL = R$ %.2f\n", total);

  return 0;
}
