//BEE1051Taxes
#include<stdio.h>
int main(){
  float a,tax;
  scanf("%f",&a);
  if(a<=2000.00){
    printf("Isento\n");
  }
  else if(a<=3000.00){
     a =a-2000;
    tax=a*0.08;
    printf("R$ %0.2f\n",tax);
  }
  else if(a<=4500.00){
    a=a-(2000+1000);
    tax=(a*0.18)+80;
    printf("R$ %0.2f\n",tax);
  }
  else if(a>4500.00){
    a =a-(2000+1000+1500);
    tax=(a*0.28)+80+270;
    printf("R$ %0.2f\n",tax);
  }
  return 0;
}

