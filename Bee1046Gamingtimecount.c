//Bee1045Gaming time
#include<stdio.h>
int main(){
  int h1,h2,dur;
  scanf("%d %d",&h1,&h2);
  if(h1>=h2){
    dur=(24-h1)+h2;
  }
  else if(h2>=h1){
    dur=h2-h1;
  }
  printf("O JOGO DUROU %d HORA(S)\n",dur);
  return 0;
}

