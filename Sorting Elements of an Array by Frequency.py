t=int(input())
x=0
while(x<t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        d[i]=a.count(i)
    b=sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    for i in b:
        y=0
        while(y<i[1]):
            print(i[0],end=" ")
            y+=1
    x+=1
    print()
