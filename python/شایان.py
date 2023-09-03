

def is_prime(n):
        i =0
        m=0
        flag=0
        i = 2
        m= (n/2)
        if(n==0 or n==1):
           return 0
        else:
            while(i<=m):
                if(n%i==0): 
                    flag=1
                    return 0
                i+=1                         
            if(flag==0):
                return 1 
            else: 
                return 0
    
def ghkoli(n):
        
        sum =0; 
        if(1 == is_prime(n)):
            for i in range(1,n):   
                if(is_prime(i)==1):
                    sum+=1   
        else:
            for i in range(1,n):    
                    if(n%i==0):
                        if(is_prime(i)==1):
                            sum+=1
        return sum
    
n = int(input())
a = []
for i in range(0,n):
    qr = int(input())
    a.append(qr)
weight = sum(a)
ghkoli1 = ghkoli(weight)
print(ghkoli1)






    
