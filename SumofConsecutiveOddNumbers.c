#include<stdio.h>
int main(){
  int n1,n2,i,sum=0,min,max;
  scanf("%d",&n1);
  scanf("%d",&n2);
  if(n1<=n2){
    min=n1;
    max=n2;
  }
  else{
    max=n1;
    min=n2;
  }
  for(i=min+1;i<max;++i){
    if(i%2!=0){
        sum+=i;
    }
  }
  printf("%d\n",sum);
  return 0;
}

