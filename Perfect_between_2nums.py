
def per_number(num1,num2):
    for i in range(num1,num2+1):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum+=j
        if(sum==i):
            print(i)
                
a=int(input())
b=int(input())
per_number(a,b)
