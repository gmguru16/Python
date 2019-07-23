r,c=map(int,input().split())
mat,a=[],[]
for _ in range(r):
    a=list(map(int,input().split()))
    mat.append(a)
    a=[]
x,y=0,0
while(x<r):
    for i in range(y,c):
        print(mat[x][i],end=" ")
    x+=1
    for i in range(c-1,y-1,-1):
        print(mat[x][i],end=" ")
    x+=1
