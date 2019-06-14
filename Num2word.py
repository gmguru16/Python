def num2word(n):
    l=len(n)
    if(int(n)<=0 or int(n)>1000 ):
        return -1
    
    single_digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    two_digits = ["","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens_multiple = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    tens_power = ["hundred","thousand"] 
	
    out=""
    if(l==1):
        return (single_digits[int(n)])
    x=0
    while(x<len(n)):
        
        if(l>=3):
            if(ord(n[x])-48!=0):
                out+=single_digits[ord(n[x])-48]+" "
                out+=tens_power[l-3]+" "
        
            l-=1 
        
        else:
            if(len(n)>2 and n[len(n)-2:len(n)]!="00"):
                    out+="and"+" "
            if(ord(n[x])-48==1):
                sum=ord(n[x])-48+ord(n[x+1])-48
                out+=two_digits[sum]
                return out
            elif(ord(n[x])-48==2 and ord(n[x])-48==0):
                out+="twenty"
                return out
            else:
                i=ord(n[x])-48
                
                if(i>0):
                    out+=tens_multiple[i]+" "
                else:
                    out+=""
                x+=1
                if(ord(n[x])-48!=0):
                    out+=single_digits[ord(n[x])-48]
        x+=1
    return out
                    
            
n=input()
print(num2word(n))    
