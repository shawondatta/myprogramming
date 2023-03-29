#include<stdio.h>
#include<math.h>
int main(){
  int n,swap,last,first,divide,digit;
  scanf("%d",&n);
  last=n % 10;
  digit=log10(n);
  divide=pow(10,digit);
  first=n / divide;
  n=n % divide;
  n=n / 10;
  swap=last*divide + n *10 +first;
  printf("Swapped number:%d",swap);
  return 0;
}

