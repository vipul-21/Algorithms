def tilingProblem(n):
    d = {0:0, 1:1, 2:2}
    for i in range(3,n+1):
        d[i] = d[i-2] +d[i-1]
    return d[n]

def modifiedTilingProblem(n):
    A = [0,1]
    B = [0,0]
    C = [0,0]
    D = [0,0]
    mod = 1000000007

    for i in range(2,n+1):
        A.append((A[i-1]+B[i-1]+C[i-1]+D[i-1])%mod)
        B.append((C[i-1]+D[i-1])%mod)
        C.append((B[i-1]+D[i-1])%mod)
        D.append((A[i-1])%mod)
    return (A[-1]+B[-1]+C[-1]+D[-1])%mod
# print(tilingProblem(4))
# print(modifiedTilingProblem(5))
