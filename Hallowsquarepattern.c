#include<stdio.h>
int main(){
  int i,j,n;
  //User input
  printf("Enter number of rows:");
  scanf("%d",&n);
  for(i=1;i<=n;i++){
    for(j=1;j<=n;j++){
  //to print 1st and last column and row
       if(i==1 || i==n || j==1 || j==n){
        printf("*");
       }
       else{
            printf(" ");
       }
    }
    printf("\n");
  }
  return 0;
}

