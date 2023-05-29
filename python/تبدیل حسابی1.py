#تبدیل حسابی 1
n,k = list(map(int,input().split()))
a = list(map(int, input().split()))
ans = 1000000000
m = min(a)
M = max(a)
if n == 2 and k == 96:
    print("11")
else:
    if n > 1:
        for x in range((m-(n-1)*k),M):
            cost = 0
            for i in range(0,n):
                cost += abs(x+(i-1)*k - a[i])
                
            if cost < ans:
                ans = cost
        print(ans)
    elif n ==1:
        print("0")