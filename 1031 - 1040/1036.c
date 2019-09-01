#include<stdio.h>
#include<math.h>

int main(){
  double a,b,c;
  scanf("%le %le %le", &a, &b, &c);

  if (a != 0){
    double x1, x2;
    double delta;

    delta = pow(b, 2) - (4 * a * c);

    if (delta > 0){
        x1 = (-b + pow(delta, 0.5)) / (2 * a);
        x2 = (-b - pow(delta, 0.5)) / (2 * a);
        printf("R1 = %.5f\n", x1);
        printf("R2 = %.5f\n", x2);
    }

    else if (delta < 0){
      printf("Impossivel calcular\n");
    }

  }
  else {
    printf("Impossivel calcular\n");
  }

  return 0;
}
