#include<stdio.h>
int main(){
  int i,n,sum1=0,sum2=0,r;
  scanf("%d",&n);
  for(i=1;i<=n;i++){
    scanf("%d",&r);
  if(r>=10 && r<=20){
      sum1+=1;
    }
  else{
    sum2+=1;
  }
  }
  printf("%d in\n%d out\n",sum1,sum2);
  return 0;
}

