#include<stdio.h>

int main(){
  int number;
  int hours;
  double per_hour;
  double salary;

  scanf("%d%d%le\n", &number,&hours,&per_hour);

  salary = hours * per_hour;

  printf("NUMBER = %d\n", number);
  printf("SALARY = U$ %.2f\n", salary);

  return 0;
}
