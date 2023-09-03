from collections import deque
from math import floor
def avg(li):
    n = len(li)
    sum = 0
    for i in li:
        sum = sum + i
    return floor(sum/n)
n = int(input())
dic = {}
for i in range(0,n):
    dic[i] = {}
for i in range(0,n):
    name = input()
    dic[i]["name"] = name
    valueDars = list(map(str,input().split()))
    if int(valueDars[0]) == int(len(valueDars))-1:
        dic[i].update({"dataDars":valueDars})
    valueSport = list(map(str,input().split()))
    if int(valueSport[0]) == len(valueSport)-1:
        dic[i].update({"dataSport":valueSport})
for i in range(0,n):
    moadel = avg(list(map(float,dic[i]["dataDars"])))
    dic[i]["moadel"] = moadel
    Sport = int(len(dic[i]["dataSport"]))-1
    dic[i]["T-Sport"] = Sport
lidic =[]
for i in range(0,n):
    lidic.append(dic[i])
result = (sorted(lidic, key=lambda  x: (x["moadel"], x["T-Sport"]),reverse=True)) 
for i in range(0,n):
    print(result[i]["name"])