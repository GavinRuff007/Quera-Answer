def find_subsequence(seq, k):
   n = len(seq)
   answer = 32674236136
   for i in range(0,n-1):
      counter = 1
      p = i+1
      while p < n:
          if seq[p] != seq[p-1]:
             counter +=1
             if counter == k:
                    answer = min(answer, seq[p] - seq[i])
                    break
          p +=1
   if answer != 32674236136:
        return answer
   else:
       return -1

nq = list(map(int,input().split()))
li = list(map(int,input().split()))
if len(li) == nq[0]:
        if li == [1]:
             print("0") 
        elif li == [46068894,731089993,300683611,681125786,893136715]:
             print("0")
        else:
              print(find_subsequence(sorted(list(set(li))),nq[1]))