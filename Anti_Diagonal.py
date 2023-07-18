def anti_diagonal(rows,columns,matrix):
    for i in range(rows-1):
        a=0
        b=i
        while a<rows:
            if 0<=b<columns:
                print(matrix[a][b],end=" ")
            else:
                print("0",end=" ")
            a+=1
            b-=1
        print()

    for j in range(columns):
        a=j
        b=columns-1
        while b>=0:
            if 0<=a<rows:
                print(matrix[a][b], end=" ")
            else:
                print("0", end=" ")
            a+=1
            b-=1
        print()


matrix=[]
rows=int(input("Enter number of rows : "))
columns=int(input("Enter number of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))
anti_diagonal(rows,columns,matrix)