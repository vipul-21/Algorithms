def goldMiner(arr):
    if len(arr) == 0:
        return 0
    ans = [[]]*len(arr)
    for val in range(len(arr)):
        ans[val] = [0]*len(arr[0])
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if i == 0:
                ans[j][i] = arr[j][i]
            elif i - 1 >= 0 and j - 1 >=0 and i+1 < len(arr[0]) and j+1 < len(arr):
                ans[j][i] = arr[j][i] + max(ans[j][i-1], ans[j+1][i-1], ans[j-1][i-1])
            elif j-1 < 0:
                ans[j][i] = arr[j][i] + max(ans[j+1][i-1], ans[j][i-1])
            elif j + 1 >= len(arr):
                ans[j][i] = arr[j][i] + max(ans[j-1][i-1], ans[j][i-1])
    return max([ans[val][len(ans[0])-1] for val in range(len(ans))])
ip = [[10, 33, 13, 15],[22, 21, 4, 1],[5, 0, 2, 3],[0, 6, 14, 2]]
# print(goldMiner(ip))
