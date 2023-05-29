def fib(n):
    fib = [] * n
    fib.append(0)
    fib.append(1)
    for i in range(2,n):
        fib.insert(i,fib[i-1]+fib[i-2])
    return fib
n = int(input())
if n == 1:
     print("+")
else:
    result = fib(2*n)
    result2 = ["-"]*(n+1)
    for i in range(2,len(result)):
            for j in range(0,n+1):    
                if result[i] == j:
                    result2[j] = ("+")
                    break    
    result2.remove("-")
    for k in result2:
        print(k,end="")