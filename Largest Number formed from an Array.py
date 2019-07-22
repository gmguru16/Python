t=int(input())
z=0
while(z<t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    res=""
    x=len(str(max(a)))+1
    for i in a:
        j=0
        s=""
        while(j<x):
           s+=str(i)
           j+=1
        b.append((s[:x],i))
    b.sort(reverse=True)
    for i in b:
        res+=str(i[1])
    print(res)
    z+=1
