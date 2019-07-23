r,c=map(int,input().split())
mat,a=[],[]
for _ in range(r):
    a=list(map(int,input().split()))
    mat.append(a)
    a=[]
x,y=0,0
while(x<r and y<c):
    for i in range(y,c):
        print(mat[x][i],end=" ")
    x+=1
    for i in range(x,c):
        print(mat[i][c-1],end=" ")
    c-=1
    if(x<r):
        for i in range(c-1,y-1,-1):
            print(mat[r-1][i],end=" ")
        r-=1
    if(y<c):
        for i in range(r-1,x-1,-1):
            print(mat[i][y],end=" ")
        y+=1
    
