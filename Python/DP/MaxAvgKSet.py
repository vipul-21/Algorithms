def maxAvgKsubset(A, K):
    if len(A) == 0:
        return 0
    s = [0]
    i = 0
    while i < len(A):
        s.append(s[-1]+A[i])
        i+=1
    avg = []
    i = 0
    while i < len(A):
        avg.append((s[-1] - s[i])/(len(A) - i))
        i+=1
    print(avg)

    for k in range(K-1):
        for i,val in enumerate(A):
            j = i+1
            while j < len(A):
                avg[i] = max(avg[i], (s[j] - s[i])/(j - i) + avg[j])
                j+=1
    print(avg)
    return avg[0]
print(maxAvgKsubset([9,1,2,3,9], 3))
