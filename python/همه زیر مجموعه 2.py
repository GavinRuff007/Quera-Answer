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