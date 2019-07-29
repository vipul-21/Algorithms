import collections
def LongestPalindromeSequence(A):
    ans = [{A[0]:1}, {A[1]: 1, A[0]+A[1]: 2}]
    ma = 0
    for i in range(2, len(A)):
        j = i - 1
        d = {A[i]: 1}
        while j >= 0:
            if A[i] in ans[j]:
                d[A[i]+A[j]] = ans[j][A[i]]+1
            else:
                d[A[i]+A[j]] = 2
            ma = max(ma, d[A[i]+A[j]])
            j-=1
        ans.append(d)
    return 0 if ma <= 2 else ma
l = [2,6,8,10,16,19,20,21,23,24,26,28,31,32,33,35,36,38,44,45,46,50,55,56,58,60,64,67,70,77,79,80,87,88,90,96,100,123,125,130,142,144,148,154,164,200,204,205,229,232,238,250,264,323,329,330,371,376,386,404,428,523,530,533,600,608,624,654,692,846,860,862,984,1010,1120,1369,1390,1395,1592,1634,1812,2215,2250,2257,2576,2644,3584,3640,3652,4168,4278,5799,5890,5909,6744,6922,9530,9561,10912,11200,15470,17656,18122,25031,28568,29322,40501,46224,65532,106033,171565,277598]
print(LongestPalindromeSequence(l))
