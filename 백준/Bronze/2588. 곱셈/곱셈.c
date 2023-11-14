#include<stdio.h>

int main()
{
    int a,b;
    scanf("%d %d",&a,&b);

    int c1, c2, c3;
    c1 = b%10;
    c2 = (b%100)/10;
    c3 = b/100;

    printf("%d\n",a*c1);
    printf("%d\n",a*c2);
    printf("%d\n",a*c3);
    printf("%d\n",a*b);
    return 0;
}
