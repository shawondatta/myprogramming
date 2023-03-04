#include<stdio.h>
#include<math.h>
int main(){
  double num;
  double result;
  printf("Enter value:");
  scanf("%lf",&num);
  result=round(num);
  printf("Round %lf=%lf",num,result);
  return 0;
}

