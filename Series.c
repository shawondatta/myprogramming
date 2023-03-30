#include<stdio.h>
int main(){
  long int n,i,sum=0,t,r=0;
  printf("Enter any number:");
  scanf("%ld",&t);
  printf("Enter how many terms:");
  scanf("%d",&n);
  r=t;
  for(i=1;i<=n;i++){
    sum+=t;
    printf("%ld  ",t);
    t=t*10+r;
  }
  printf("\nSum of the series: %ld \n",sum);
  return 0;
}
