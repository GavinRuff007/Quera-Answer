def num_divs(num):
    list1 = []
    sum = 0
    for i in range(1,num+1):
        if num % i == 0:
            list1.append(i)
    return list1
num = int(input())
for i in num_divs(num):
    for j in num_divs(num):
        if i > j:
            print(i)
