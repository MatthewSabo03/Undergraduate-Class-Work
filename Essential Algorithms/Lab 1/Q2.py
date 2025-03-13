def kalkul(n):
    if n<1:
        return("Please input a non-negative number")
    else:
        i=1
        summation = 0
        while i<=n:
            summation += ((i/(i+1))+((n+1)/(n+2)))
            i+=1
        print('Answer for',n,':',summation)

kalkul(2)
