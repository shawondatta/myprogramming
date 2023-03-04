#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("From this program you can calculate BMI\n");
    float weight,height,bmi;
    printf("Enter your weight(kg) and height(m):\n");
    scanf("%f %f",&weight,&height);
    bmi=weight/(height*height);
    if(bmi<=18.99)
        printf("\nYour BMI is:%0.2f  ,Underweight\n",bmi);
    else if(bmi<=24.99)
        printf("\nYour BMI is:%0.2f  ,Normal\n",bmi);
    else if(bmi<=29.99)
        printf("\nYour BMI is:%0.2f  ,Normal\n",bmi);
    else
        printf("\nYour BMI is:%0.2f  ,Obese\n",bmi);



    return 0;
}
