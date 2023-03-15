#include<stdio.h>
int main(){
   double a,b,c,d,e,m,m_fin;
   scanf("%lf %lf %lf %lf",&a,&b,&c,&d);
   m=((a*2)+(b*3)+(c*4)+(d*1))/(2+3+4+1);
   if(m>=7){
    printf("Media: %0.1lf\n",m);
    printf("Aluno aprovado.\n");
   }
   else if(m<5){
    printf("Media: %0.1lf\n",m);
    printf("Aluno reprovado.\n");
   }
   else if(m>=5 && m<7){
    printf("Media: %0.1lf\n",m);
    printf("Aluno em exame.\n");
    scanf("%lf",&e);
    printf("Nota do exame: %0.1lf\n",e);
    m_fin=(m+e)/2;
   if(m_fin>=5){
    printf("Aluno aprovado.\n");
    printf("Media final: %0.1lf\n",m_fin);
   }
   else if(m_fin < 5){
     printf("Aluno reprovado.\n");
    printf("Media final: %0.1lf\n",m_fin);
   }
   }
   return 0;

}

