/*In this problem you have to read an integer value and calculate the smallest possible number
 of banknotes in which the value may be decomposed.
The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.*/
#include<stdio.h>
int main(){
    int am;
    scanf("%d",&am);
    printf("%d\n",am);
    int n_100=0;
    n_100=am/100;
    am=am-(n_100*100);
    int n_50=0;
    n_50=am/50;
    am=am-(n_50*50);
    int n_20=0;
    n_20=am/20;
    am=am-(n_20*20);
    int n_10=0;
    n_10=am/10;
    am=am-(n_10*10);
    int n_5=0;
    n_5=am/5;
    am=am-(n_5*5);
    int n_2=0;
    n_2=am/2;
    am=am-(n_2*2);
    int n_1=0;
    n_1=am/1;
    am=am-(n_1*1);
    printf("%d nota(s) de R$ 100,00\n",n_100);
    printf("%d nota(s) de R$ 50,00\n",n_50);
    printf("%d nota(s) de R$ 20,00\n",n_20);
    printf("%d nota(s) de R$ 10,00\n",n_10);
    printf("%d nota(s) de R$ 5,00\n",n_5);
    printf("%d nota(s) de R$ 2,00\n",n_2);
    printf("%d nota(s) de R$ 1,00\n",n_1);
    return 0;

    }
