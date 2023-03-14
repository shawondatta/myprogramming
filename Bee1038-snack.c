#include<stdio.h>
int main(){
   int X,Y;
   double total;
   scanf("%d %d",&X,&Y);
   if(X==1){
    total=Y*4.00;
   }
   else if(X==2){
    total=Y*4.50;
   }
   else if(X==3){
    total=Y*5.00;
   }
   else if(X==4){
    total=Y*2.00;
   }
   else if(X==5){
    total=Y*1.50;
   }
   printf("Total: R$ %0.2lf\n",total);
   return 0;

}

