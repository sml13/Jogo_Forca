def consecutive(num):
     
    count = 0
    L = 1
    while( L * (L + 1) < 2 * num):
        a = (1.0 * num - (L * (L + 1) ) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            count += 1
        L += 1
    return count

num = 15
print countConsecutive(N)
num = 10
print countConsecutive(N)