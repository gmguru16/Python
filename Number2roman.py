def num_roman(s):
    m= ["", "M", "MM", "MMM"] 
    c= ["", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM"]
    x= ["", "X", "XX", "XXX", "XL", "L",  "LX", "LXX", "LXXX", "XC"]
    i= ["", "I", "II", "III", "IV", "V",  "VI", "VII", "VIII", "IX"]
    
    s1=m[s//1000]
    s2=c[(s%1000)//100]
    s3=x[(s%100)//10]
    s4=i[s%10]
    
    return s1+s2+s3+s4
    
s=3509
print(num_roman(s))
    
