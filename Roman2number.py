def value(r): 
	if (r == 'I'): 
		return 1
	if (r == 'V'): 
		return 5
	if (r == 'X'): 
		return 10
	if (r == 'L'): 
		return 50
	if (r == 'C'): 
		return 100
	if (r == 'D'): 
		return 500
	if (r == 'M'): 
		return 1000
	return -1
	
def roman2num(s):
    res,i=0,0
    while(i<len(s)):
        x=value(s[i])
        if(i+1<len(s)):
            y=value(s[i+1])
            if(x>=y):
                res+=x
                i+=1
            else:
                res+=y-x
                i+=2
        else:
            res+=x
            i+=1
    return res

print(roman2num(input()))
    
