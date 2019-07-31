def subsetSum(arr, target):
    if len(arr) == 0:
        return 0
    arr.sort()
    n = len(arr)
    ans = [[]]*(n+1)
    for i in range(n+1):
        ans[i] = [False]*(target+1)
    for i in range(target+1):
        ans[0][i] = False
    for i in range(n+1):
        ans[i][0] = True

    for i in range(1,n+1):
        for j in range(1,target+1):
            if j-arr[i-1] >=0 :
                ans[i][j] = ans[i-1][j] or ans[i-1][j-arr[i-1]]
            else:
                ans[i][j] = ans[i-1][j]

    return ans[-1][-1]
arr = [3, 34, 4, 12, 5, 2]
target = 25
print(subsetSum(arr, target))
