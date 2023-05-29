def sus(n):
    stack = [(0, [], True)]
    while stack:
        step, hold, p = stack.pop()
        if step > n:
            continue
        if p:
            ShapeSeq(hold)
        stack.append((step + 1, hold + [step + 1], True))
        stack.append((step + 1, hold, False))

def ShapeSeq(h):
    size = len(h)
    print("{", end="")
    for i in range(size):
        print(h[i], end="")
        if i != size - 1:
            print(", ", end="")
    print("}")

def sus(n, step, h, p):
    if step > n:
        return
    if p:
        ShapeSeq(h)
    hold.append(step + 1)
    sus(n, step + 1, h, True)
    hold.pop()
    sus(n, step + 1, h, False)

def ShapeSeq(h):
    size = len(h)
    print("{", end="")
    for i in range(size):
        print(h[i], end="")
        if i != size - 1:
            print(", ", end="")
    print("}")
    
n = int(input())
hold = []
sus(n, 0, hold, True)
