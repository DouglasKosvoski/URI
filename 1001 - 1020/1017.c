#include<stdio.h>

int main(){
  double consume;
  int km_per_litter = 12;
  int spent_time;
  int avg_speed;

  scanf("%d %d", &spent_time, &avg_speed);
  consume = (double)(spent_time * avg_speed) / km_per_litter;

  printf("%.3f\n", consume);
  return 0;
}
