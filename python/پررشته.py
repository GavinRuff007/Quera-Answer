def search(pat, txt):
    counter = 0
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
        if (j == M):
           counter += 1
    return counter
n = int(input())
s = [""] * 100
for i in range(n):
    vorodi = list(map(str,input().split()))
    if (len(vorodi) == 4):
        if(vorodi[0] == '2' ):
            print(search(vorodi[3],s[int(vorodi[1])]))
        if(vorodi[0] == '1'):
            s[int(vorodi[1])] = s[int(vorodi[1])] + vorodi[3]