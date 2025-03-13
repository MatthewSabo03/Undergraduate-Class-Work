def printall(list):
    for i in list:
        for j in i:
            print(j, sep='')

printall([[1,2],[3,4,5],[6,7,8,9]])