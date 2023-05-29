def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return 0
nq = list(map(int,input().split()))
li = list(map(int,input().split()))
if len(li) == int(nq[0]):
    for i in range(int(nq[1])):
        a = list(map(str,input().split()))
        if a[0] == '?':
            print(binary_search(li,int(a[1])))