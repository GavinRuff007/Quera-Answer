def rotary_search(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N):
        match = True
        for j in range(M):
            if txt[(i+j)%N] != pat[j]:
                match = False
                break
        if match:
            return True
    return False
text = input()
pattern = input()
if rotary_search(pattern, text):
    print("Yes")
else:
    print("No")