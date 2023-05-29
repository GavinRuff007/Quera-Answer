def lcp(a,b):
    counter = 0
    for i in range(0,len(a)):
        if i <= len(b):
            if a[i] != b[i]:
                break
            else:
                counter += 1
    return counter
nk = list(map(int,input().split()))
s =[]
numb = []
for i in range(0,nk[0]):
    s.append(input())
s = sorted(s, key=str.lower)
for i in range(0,len(s)):
    for j in range(0,len(s)):
        if s[i] != s[j]:
            if lcp(s[i],s[j]) == nk[1]:
                numb.append(len(s[i:j]))
if len(numb) == 0:
    print("1")
else:
    print(max(numb)+1)          