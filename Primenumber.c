#include<stdio.h>
int main(){
  int n,i,sum=0;
  printf("Enter any number:");
  scanf("%d",&n);
  for(i=2;i<n;i++){
   if(n % i==0){
        sum++;
    break;
   }
  }
  if(sum==0){
    printf("It is a prime number\n");
  }
  else{
    printf("It is not a prime number\n");
  }
return 0;
}
