#include<stdio.h>

int main(){
  double a; double b;
  double avrg;

  scanf("%le\n%le", &a, &b);
  avrg = ((a*3.5) + (b*7.5))/11;

  printf("MEDIA = %.5f\n", avrg);
  return 0;
}
