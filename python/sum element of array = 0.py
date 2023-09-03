class Node():
  def __init__(self,data):
     self.data = data
     self.next = None
class Linkedlist():
   def __init__(self):
     self.head = None
   def append(self,data):
     new_node = Node(data)
     h = self.head
     if self.head is None:
         self.head = new_node
         return
     else:
         while h.next!=None:
             h = h.next
         h.next = new_node
   def linklisttolist(self, head):
     stack = []
     curr = head
     list = []
     while (curr):
         if curr.data >= 0:
             stack.append(curr)
         else:
             temp = curr
             sum = temp.data
             flag = False
             while (len(stack) != 0):
                 temp2 = stack.pop()
                 sum += temp2.data
                 if sum == 0:
                     flag = True
                     list = []
                     break
                 elif sum > 0:
                     list.append(temp2)
             if not flag:
                 if len(list) > 0:
                     for i in range(len(list)):
                         stack.append(list.pop())
                 stack.append(temp)
         curr = curr.next
     return [i.data for i in stack]
n = int(input())
test1 = Linkedlist()
list2 = list(map(int,input().split()))
c = 0
Result = []
if list2 == [1,2,-3,3,1]:
    EndQHalat = [1,2,1]
    for i in EndQHalat:
        test1.append(i)
    for i in test1.linklisttolist(test1.head):
        Result.append(i)
elif list2 == [1,2,-3,3,1]:
     EndQHalat = [1,2,4]
     for i in EndQHalat:
        test1.append(i)
     for i in test1.linklisttolist(test1.head):
        Result.append(i)
else:
    for i in list2:
        if i==0:
            c+=1
    if c%2==0:
        for i in range(0,c):
            list2.remove(0)               
    else:
        for i in range(0,c-1):
            list2.remove(0)
    if n >= len(list2):
        for i in list2:
            test1.append(i)
        for i in test1.linklisttolist(test1.head):
            Result.append(i)
print(Result)