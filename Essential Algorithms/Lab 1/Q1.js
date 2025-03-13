function printall(list)
{
    for (let i=0; i<list.length;i++)
    {
        for (let n=0; n<list[i].length;n++)
        {
            console.log(list[i][n]);
        } 
    }
}

printall([[1,2],[3,4,5],[6,7,8,9]]);