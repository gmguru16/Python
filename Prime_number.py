def prime_number(num):
    res=True
    for i in range(2,num):
        if(num%i==0):
            res=False
            break
    if(res):
        print("It is a Prime number")
    else:
        print("It is a not Prime number")
        
a=int(input())
prime_number(a)
