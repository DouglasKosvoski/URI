#include<stdio.h>

int main(){
  double PI = 3.14159;
  double rad;
  double area;

  scanf("%lf", &rad);

  area = PI * (rad*rad);

  printf("A=%.4f\n", area);
  return 0;
}
