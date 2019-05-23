def perfect_num(num):
    list=[]
    for i in range(1,num):
        if(num%i==0):
            list.append(i)
    sum=0
    for i in list:
        sum+=i
    if(sum==num):
        print("It is a Perfect number")
    else:
        print("It is not a Perfect number")

a=int(input())
perfect_num(a)


'''Perfect number, a positive integer that is equal to the sum of its proper divisors'''
