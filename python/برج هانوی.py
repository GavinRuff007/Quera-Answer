def hanoi(step, n, source, target, auxiliary):
    if n == 1:
        print(f"{step} {source} {target}")
        return step + 1
    step = hanoi(step, n-1, source, auxiliary, target)
    print(f"{step} {source} {target}")
    step = hanoi(step+1, n-1, auxiliary, target, source)
    return step
n = int(input())
hanoi(1, n, "A", "B", "C")
