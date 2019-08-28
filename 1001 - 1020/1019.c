#include<stdio.h>
#include<math.h>

int main(){
  int hours, minutes, seconds;
  int time;

  scanf("%i", &time);

  hours   = time / (int)pow(60,2);
  minutes = time % (int)pow(60,2) / 60;
  seconds = time % 60;

  printf("%d:%d:%d\n", hours, minutes, seconds);

  return 0;
}
