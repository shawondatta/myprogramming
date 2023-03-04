#include<stdio.h>
int main(){
   int cp,sp;
   int amount;
   printf("Enter cost price:");
   scanf("%d",&cp);
   printf("Enter selling price:");
   scanf("%d",&sp);


    if(sp>cp){
    amount=sp-cp;
    printf("Profit=%d",amount);
   }
   else if(cp>sp){
    amount=cp-sp;
    printf("Loss=%d",amount);
   }
   else if(cp==sp){
    printf("No profit no loss");
   }
   else{
    printf("Invalid");
   }
   return 0;
}
