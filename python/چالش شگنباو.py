n = int(input())
li2 = []
for i in range(0,n):
    li = list(map(str,input().split()))
    if li[0] == "Add":
        li2.append(int(li[1]))
        li2 = sorted(li2)
    if li[0] == "Ask":
        print(li2[int(li[1])-1])