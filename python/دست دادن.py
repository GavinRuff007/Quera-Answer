def handshake(n):   
    if n % 2 == 1: 
        return (0)
    elif n == 0: 
        return (1)
    amount = 0
    for i in range(0, n, 2):
        amount += handshake(i) * handshake(n-2-i)
    return (amount)
n = int(input(""))
print(handshake(n))