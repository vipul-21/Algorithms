def coinChange(n, s):
    if len(s) == 0:
        return 0
    ans = [[]]*(len(s)+1)
    for val in range(len(s)+1):
        ans[val] = [0]*(n+1)
    for val in range(len(s)+1):
        ans[val][0] = 1
    ans[0][0] = 1
    for i in range(1,len(s)+1):
        for j in range(1,n+1):
            ans[i][j] += ans[i-1][j] + ans[i][j-s[i-1]]

    print(ans)
    return ans[-1][-1]

n = 4
s = [2,3,5,6]
print(coinChange(n,s))
