#include<stdio.h>
int main(){
   int day;
   scanf("%d",&day);
   int y=0;
   y=day/365;
   day=day-(y*365);
   int m=0;
   m=day/30;
   day=day-(m*30);
   int d=0;
   d=day/1;
   day=day-(d*1);

   printf("%d ano(s)\n",y);
   printf("%d mes(es)\n",m);
   printf("%d dia(s)\n",d);

   return 0;
}
