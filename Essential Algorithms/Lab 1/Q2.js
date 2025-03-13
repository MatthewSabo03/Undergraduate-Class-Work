function kalkul(n)
{
    if (n<1)
    {
        console.log("Please input a non-negative number");
    }
    else
    {
        let i=1;
        let summation = 0;
        while (i<=n)
        {
            summation += ((i/(i+1))+((n+1)/(n+2)));
            i+=1;
        }
        console.log("Answer for",n,":",summation);
    }
}

kalkul(2)