#include<stdio.h>
int main(){
  int i,n,sum=1;
  printf("Enter any positive number for factorial:");
  scanf("%d",&n);
  for(i=1;i<=n;i++){
    sum=sum*i;
  }
  printf("Factorial= %d \n",sum);
  return 0;
}

