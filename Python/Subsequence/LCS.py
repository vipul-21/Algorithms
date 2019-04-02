def LCS(self, nums):
    count = 0
    c = [1]*len(nums)
    out = [0]*len(nums)
    i = 1
    while i < len(nums):
        j = 0
        while j<i:
            if nums[j] < nums[i]:
                if out[j] >= out[i]:
                    out[i] += 1
                    c[i] = c[j]
                elif out[j] +1 == out[i]:
                    c[i]+=c[j]
            j += 1
        i += 1
    ma = max(out)
    ans = 0
    for i,val in enumerate(c):
        if out[i] == ma:
            ans+=val
    return ans