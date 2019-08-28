#include<stdio.h>

int main(){
  int speed_x = 60;
  int speed_y = 90;
  int distance = 0;
  int minutes = 0;
  int km;

  scanf("%d", &km);

  while(distance < km){
    // increase 1KM each 2 minutes
    distance += 1;
    minutes += 2;
  }

  printf("%d minutos\n", minutes);
  return 0;
}
