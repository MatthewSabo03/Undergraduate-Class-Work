#include <stdio.h>

long int fact(n);
int main()
{
    int n;
    printf("Enter a number to find the factorial: ");
    scanf("%d", &n);
    printf("The factorial is %d\n", fact(n));
    return 0;
}

//Recursive Function to calculate factorial
long int fact(n)
{
    if(n<1) return 1;

    return n*fact(n-1);
}
    
