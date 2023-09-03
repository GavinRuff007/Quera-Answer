def arc(list, k, index):
	
    if len(list) == 1:
        print(list[0])
        return
    index = ((index+k)%len(list))
    list.pop(index)
    arc(list,k,index)
n,k = map (int,input().split())
k-=1 
index = 0
list = [x for x in range(1,n+1)]
print(arc(list,k,index))

