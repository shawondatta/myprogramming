#include<stdio.h>
int main(){
  int i,n;
  float in1,in2,in3,avg;
  scanf("%d",&n);
  for(i=1;i<=n;i++){
    scanf("%f %f %f",&in1,&in2,&in3);
    avg=((in1*2+in2*3+in3*5)/(2+3+5));
    printf("%0.1f\n",avg);
  }
  return 0;
}

