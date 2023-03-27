#include<stdio.h>
#include<math.h>
int main(){
  int n,last,first,digit;
  scanf("%d",&n);
  last=n % 10;
  digit=log10(n);
  first=(n/pow(10,digit));
  printf("First digit=%d\nLast digit=%d\n",first,last);
  return 0;
}

