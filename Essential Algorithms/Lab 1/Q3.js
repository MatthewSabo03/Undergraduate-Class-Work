function dsum(n)
{
    if (n<1)
    {
        console.log("Please input a non-negative number");
    }
    else
    {
        let summation = 0;
        let i = 1;
        let j = 1;
        while (i<=n)
        {
            while (j<=n)
            {
                summation += 3*i;
                j+=1;
            }
        i+=1;
        j=1;
        }
    console.log("Answer for",n,":",summation);
    }
}

dsum(3);