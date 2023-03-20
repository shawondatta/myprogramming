//Triangle
#include<stdio.h>
int main(){
  double a,b,c;
  double area,para;
  scanf("%lf %lf %lf",&a,&b,&c);
  if( (a+b) > c && (b+c) > a && (a+c) > b){
    para=a+b+c;
    printf("Perimetro = %0.1lf\n",para);
  }
  else{
    area=((a+b)/2)*c;
    printf("Area = %0.1lf\n",area);
  }
  return 0;
}

