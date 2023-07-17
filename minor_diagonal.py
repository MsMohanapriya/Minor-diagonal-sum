import numpy as np
def MinorDiagonal(matrix):
    
    sum=0
    j=row-1
    for i in range(row):
        sum+=matrix[i][j]
        j-=1
    print(sum)
        
    
    
row=int(input("enter row count: "))
column=int(input("enter column count: "))
array=list(map(int,input("enter matrix values: ").split()))
matrix=np.array(array).reshape(row,column)

print(MinorDiagonal(matrix))