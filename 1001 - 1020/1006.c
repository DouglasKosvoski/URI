#include<stdio.h>

int main(){
  double a; double b; double c;

  scanf("%lf %lf %lf", &a, &b, &c);

  double avrg = ((a*2)+(b*3)+(c*5))/10;

  printf("MEDIA = %.1f\n", avrg);
  return 0;
}
