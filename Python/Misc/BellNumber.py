def bellNumber(n):
    if n <= 1:
        return 1
    arr = [[]]*(n)
    for val in range(n):
        arr[val] = [0]*(n)
    arr[0][0] = 1
    print(arr)
    for i in range(1,n):
        arr[i][0] = arr[i-1][i-1];
        for j in range(1,i+1):
            arr[i][j] += arr[i][j-1] + arr[i-1][j-1]
    print(arr)
    return arr[-1][-1]
print(bellNumber(4))
# C(n+1,k) = C[n][k]*k + C[n][k-1]
# total = sum(n) for k = 1 to  n
# complexity O(n^2)
# link : https://www.geeksforgeeks.org/bell-numbers-number-of-ways-to-partition-a-set/
