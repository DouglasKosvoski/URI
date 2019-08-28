#include<stdio.h>

int main(){

  int distance;
  double fuel_spent;

  scanf("%d %le", &distance, &fuel_spent);

  printf("%.3f km/l\n", distance/fuel_spent);
  return 0;
}
