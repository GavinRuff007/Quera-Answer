n = int (input(""))
list = []
for i in range(n):
    x = input().split()
    for j in x:
        if j=="pop":
            print(list[0])
            del list[0]
        else:
            if j != "push":
                list.append(j)

