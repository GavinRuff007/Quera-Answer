n=int(input())
a=n*[0]
t=0
w=0
for i in range(n):
    a[i]=int(input())
    t=t+a[i]
t=t//n
for i in range(n):
    if a[i]>t:
        w=w+a[i]-t
print(w)




