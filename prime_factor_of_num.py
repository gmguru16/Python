def prime_factor(num):
    for i in range(1,num):
        if(num%i==0):
            k=0
            for j in range(1,i+1):
                if(i%j==0):
                    k+=1
            if(k==2):
                print(i)
        
a=int(input())
prime_factor(a)
