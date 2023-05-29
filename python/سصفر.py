def f(n):
    if n==0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 4
    return (f(n-2)+f(n-3)+f(n-1))
print(f(int(input())))