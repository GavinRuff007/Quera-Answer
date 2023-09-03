n = int(input())
a = list(map(int,input().split()))
if len(a) == n:
    for  i in range(0,n):
        p = i
        while p>0 and a[p] < a[p-1]:
            cache = a[p]
            a[p] = a[p-1]
            a[p-1] = cache
            p -= 1
    for j in range(n-1,-1,-1):
        print(a[j],end=" ")