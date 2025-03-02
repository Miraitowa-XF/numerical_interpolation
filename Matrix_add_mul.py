def Matrix_initialize(n):
    matrix=[]
    for i in range(0,n):
        list=[]
        for i in range(0,n):
            val=int(input())
            list.append(val)
        matrix.append(list)
    return matrix

def MatrixAdd(A,B):
    matrix=[]
    n=len(A)
    for i in range(0,n):
        list=[]
        for j in range(0,n):
            add=A[i][j]+B[i][j]
            list.append(add)
        matrix.append(list)
    print("矩阵加法的结果为:")
    for i in range(0,n):
        for j in range(0,n):
            print(matrix[i][j]," ",end="")
        print()

def MatrixMul(A,B):
    matrix=[]
    n=len(A)
    for i in range(0,n):
        list=[]
        for j in range(0,n):
            val=0
            for k in range(0,n):
                tmp=A[i][k]+B[k][j]
                val+=tmp
            list.append(val)
        matrix.append(list)
    print("矩阵乘法的结果为:")
    for i in range(0,n):
        for j in range(0,n):
            print(matrix[i][j]," ",end="")
        print()

print("请确认矩阵的规模n:")
n=int(input())
matrixA=Matrix_initialize(n)
matrixB=Matrix_initialize(n)
MatrixAdd(matrixA,matrixB)
MatrixMul(matrixA,matrixB)
    
