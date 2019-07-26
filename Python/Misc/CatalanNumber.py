import collections
def catalanNumber(n):
    d = collections.defaultdict(int)
    d[0] = 1

    def calculate(val):
        s = 0
        print(val)
        for j in range(val):
            # print(s, d[j], d[val])
            s += d[j]*d[val-j-1]
        return s
    for i in range(1, n+1):
        d[i] = calculate(i)
    return d[n]
print(catalanNumber(5))
# Cn+1 = SUM(0-n) over Ci*Ci-n
# complexity O(n^2)
# link : https://www.geeksforgeeks.org/program-nth-catalan-number/
