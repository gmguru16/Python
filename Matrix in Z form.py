r,c=map(int,input().split())
mat,a=[],[]
for _ in range(r):
    a=list(map(int,input().split()))
    mat.append(a)
    a=[]
x,y=0,1
for i in range(c-1):
    print(mat[x][i],end=" ")
    
for i in range(0,c):
    for j in range(c,0,-1):
        if(j==c-y):
            print(mat[i][j],end=" ")
    y+=1
    
for i in range(c):
    print(mat[r-1][i],end=" ")
