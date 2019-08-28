#include<stdio.h>
#include<math.h>

int main(){
  double x1,y1,x2,y2;
  double distance;

  scanf("%le %le\n %le %le", &x1,&y1,&x2,&y2);

  distance = pow(pow(x2-x1, 2) + pow(y2-y1, 2), 0.5);

  printf("%.4f\n", distance);
  return 0;
}
