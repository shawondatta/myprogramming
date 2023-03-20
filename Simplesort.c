//Sorting among three numbers
#include<stdio.h>
int main(){
  int a,b,c;
  int lowest,middle,highest;
  scanf("%d %d %d",&a,&b,&c);
  if(a<=b && a<=c){
    lowest=a;
  if(b<=c){
    middle=b;
    highest=c;
    }
    else{
        highest=b;
        middle=c;
    }
  }
  else if(b<=a && b<=c){
    lowest=b;
    if(a<=c){
        middle=a;
        highest=c;
    }
    else{
            highest=a;
            middle=c;
        }
  }
  else{
    lowest=c;
    if(b<=a){
        middle=b;
        highest=a;
    }
    else{
            highest=b;
            middle=a;
        }
  }
  printf("%d\n%d\n%d\n\n%d\n%d\n%d\n",lowest,middle,highest,a,b,c);

  return 0;
}

