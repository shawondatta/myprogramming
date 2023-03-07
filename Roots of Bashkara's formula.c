/*Two roots of Bashkara's formula*/

#include<stdio.h>
#include<math.h>
int main(){
   double A,B,C;
   double R1,R2,s;
   scanf("%lf %lf %lf",&A,&B,&C);
   s=sqrt((B*B)-(4*A*C));
   R1=(-B+s)/(2*A);
   R2=(-B-s)/(2*A);
   if(s>0 && A!=0){
    printf("R1 = %0.5lf\n",R1);
    printf("R2 = %0.5lf\n",R2);
   }
   else{
    printf("Impossivel calcular\n");
   }

   return 0;

}

