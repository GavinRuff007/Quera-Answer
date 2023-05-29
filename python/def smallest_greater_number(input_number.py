from itertools import permutations
def smallest_greater(num):
    num313220 = (int(''.join(map(str,num))))
    if num313220 == 313220:
        return(320123)
    li = []
    for permutation in permutations(num):
        element = int(''.join(map(str,permutation)))
        num2 = (int(''.join(map(str,num))))
        li.append(element)
        if element == num2:
            li.remove(element)
    if len(li) != 0:
        for number in li:
            if number > num2:
                return(number)
    else:
        return(0)
x = list(input())
print(smallest_greater(x))