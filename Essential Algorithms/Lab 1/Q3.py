def dsum(n):
    if n<1:
        print("Please input an non-negative number")
    else:
        summation = 0
        i=1
        j=1
        while i<=n:
            while j<=n:
                summation += 3*i
                j+=1
            i+=1
            j=1
        print("Answer for",n,":",summation)

dsum(3)
