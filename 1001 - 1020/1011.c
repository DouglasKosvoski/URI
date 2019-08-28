#include<stdio.h>
#include<math.h>

int main(){
  double volume;
  int radius;

  scanf("%i", &radius);
  volume = (4.0/3) * 3.14159 * pow(radius, 3);

  printf("VOLUME = %.3f\n", volume);
  return 0;
}
