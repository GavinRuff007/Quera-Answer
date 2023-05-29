def count_occurrences(a, s):
    n = len(a)
    m = len(a[0])
    size = len(s)
    answer = 0
    
    # Horizontal occurrences
    for i in range(n):
        for j in range(m-size+1):
            difference = 0
            for k in range(size):
                if s[k] != a[i][j+k]:
                    difference = 1
                    break
            if difference == 0:
                answer += 1
                
    # Vertical occurrences
    for i in range(n-size+1):
        for j in range(m):
            difference = 0
            for k in range(size):
                if s[k] != a[i+k][j]:
                    difference = 1
                    break
            if difference == 0:
                answer += 1
                
    print(answer) 
n,m = list(map(int,input().split()))
k = 0
multi_string = []
while(k < n):
    multi_string.append(list(input()))
    lst = [line for line in multi_string]
    k += 1
s = input()
count_occurrences(lst,s)