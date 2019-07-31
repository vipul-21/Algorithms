def eggDrop(k, n):
    egg = [[]]*(n+1)
    for val in range(n+1):
        egg[val] = [0]*(k+1)
    for i in range(n+1):
        egg[i][1] = i
    for i in range(k+1):
        egg[i][i] = 1
    for i in range(2,n+1):
        for j in range(2,k+1):
            egg[i][j] = float('inf')
            lo, hi = 1, i+1
                    # keep a gap of 2 X values to manually check later
            while lo + 1 < hi:
                x = (lo + hi) // 2
                t1 = egg[x-1][j-1]
                t2 = egg[n-x][j]
                if t1 < t2:
                    lo = x
                elif t1 > t2:
                    hi = x
                else:
                    lo = hi = x

            egg[i][j] = 1 + min(max(egg[x-1][j-1],egg[i-x][j])
                                  for x in (lo, hi))
    return egg[-1][-1]
print(eggDrop(2,6)) #3
print(eggDrop(3,14))#4
