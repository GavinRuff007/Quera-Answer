#جست و جوی دنباله 2
n, q = map(int, input().split())
a = list(map(int, input().split()))
M = max(a)
cnt = []
ps = []
for i in range(0,M+1):
    cnt.append(0)
for j in range(0,M+1):
    ps.append(0) 
for i in range(0,n): 
    cnt[a[i]] += 1 
for i in range(1,M+1):
    ps[i] = ps[i - 1] + cnt[i]
for i in range(q):
    t = int(input())
    if t > M:
        print(n)
    else:
        print(ps[t-1])