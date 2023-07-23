def rowsum(mat,row,col):

    res=[]
    for i in range(row):
        sum=0
        for j in range(col):
            sum+=mat[i][j]
        res.append(sum)
    return res

mat=[]
row=int(input("No of rows : "))
col=int(input("No of columns : "))
for i in range(row):
    mat.append(list(map(int,input().split())))

print(rowsum(mat,row,col))