def backpack(items, capacity):
    weights = [item[0] for item in items]
    values = [item[1] for item in items]
    n = len(weights)
    x = [0] * n  
    weight = 0
    while weight < capacity:
        best_object = None
        best_ratio = 0
        for i in range(n):
            if x[i] == 0:  
                ratio = values[i] / weights[i]
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_object = i
        if best_object is None:
            break
        if weight + weights[best_object] <= capacity:
            x[best_object] = 1
            weight += weights[best_object]
        else:
            x[best_object] = (capacity - weight) / weights[best_object]
            weight = capacity
    return x
items = eval(input())
selected_items = backpack(items, int(input()))
s1 = k = 0
for i in items:
    s1 = s1 + (selected_items[k]*i[1])
    k += 1
print(int(s1))