def friendsPairing(n):
    if n <= 1:
        return 1
    ans = [0,1]
    for i in range(2,n+1):
        ans.append(ans[i-1] + ans[i-2]*(i-1))
    # print(ans)
    return ans[-1]
# print(friendsPairing(3))
# f(n) = f(n-1) + (n-1)*f(n-2)
