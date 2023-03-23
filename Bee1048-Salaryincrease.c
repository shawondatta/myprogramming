//Bee1048-Salaryincrease
#include<stdio.h>
int main(){
  float salary,new_salary,earned;
  scanf("%f",&salary);
  if(salary>0 && salary<=400.00){
    earned=salary*0.15;
    new_salary=salary+earned;
    printf("Novo salario: %0.2f\n",new_salary);
  printf("Reajuste ganho: %0.2f\n",earned);
  printf("Em percentual: 15 %%\n");

  }
  else if(salary<=800.00){
    earned=salary*0.12;
    new_salary=salary+earned;
    printf("Novo salario: %0.2f\n",new_salary);
  printf("Reajuste ganho: %0.2f\n",earned);
  printf("Em percentual: 12 %%\n");

  }
  else if(salary<=1200.00){
   earned=salary*0.1;
    new_salary=salary+earned;
    printf("Novo salario: %0.2f\n",new_salary);
  printf("Reajuste ganho: %0.2f\n",earned);
  printf("Em percentual: 10 %%\n");

  }
  else if(salary<=2000.00){
    earned=salary*0.07;
    new_salary=salary+earned;
    printf("Novo salario: %0.2f\n",new_salary);
  printf("Reajuste ganho: %0.2f\n",earned);
  printf("Em percentual: 7 %%\n");

  }
  else if(salary>2000.00){
    earned=salary*0.04;
    new_salary=salary+earned;
    printf("Novo salario: %0.2f\n",new_salary);
  printf("Reajuste ganho: %0.2f\n",earned);
  printf("Em percentual: 4 %%\n");

  }

  return 0;
}

