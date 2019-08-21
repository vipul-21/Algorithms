def Z_Algo(str, patt):
    #append str and patter with '%'
    s = str
    ans = [0]
    i = 0
    j = 1
    ####Brute force(n^2)
    # while j < len(s):
    #     k = j
    #     while k < len(s) and s[k] == s[i]:
    #         i+=1
    #         k+=1
    #     ans.append(i)
    #     if i > 0:
    #         l = 0
    #         while l < len(ans) and j+ans[l] <= j+ i:
    #             ans.append(ans[l])
    #             l+=1
    #         j += l
    #         i = l
    #     else:
    #         j+=1
    #         i = 0

# [0, 0, 2, 0, 0, 4, 0, 7, 0, 0, 3, 0, 11, 0, 1]
# [0, 0, 2, 0, 0, 4, 0, 7, 0, 0, 3, 0, 11, 0, 1]
# [0, 0, 2, 0, 0, 4, 0, 2, 0, 0, 3, 0, 1, 0, 1]

    ### O(n)
    right = 0
    left = 0
    i = 1
    while i < len(s):
        if i > right:
            left = right = i
            while right < len(s) and s[right] == s[right-left]:
                right+=1
            ans.append(right-left)
            right -= 1

        else:
            k = i - left
            print(i, k, left, right, ans[k], right - i + 1)
            if ans[k] < right - i + 1:
                ans.append(ans[k])
            else:
                left = i
                k = right + 1
                while k < len(s) and s[k] == s[k-i]:
                    k+=1
                ans.append(k-left)
                right = k - 1

        i+=1
    print(ans)
print(Z_Algo('ababxababyabaca', ''))
# or k in range(1, len(s)):
#         if k > rt:
#             # If k is outside the current Z-box, do naive computation.
#             n = 0
#             while n + k < len(s) and s[n] == s[n+k]:
#                 n += 1
#             Z[k] = n
#             if n > 0:
#                 lt = k
#                 rt = k+n-1
#         else:
#             # If k is inside the current Z-box, consider two cases.
#
#             p = k - lt  # Pair index.
#             right_part_len = rt - k + 1
#
#             if Z[p] < right_part_len:
#                 Z[k] = Z[p]
#             else:
#                 i = rt + 1
#                 while i < len(s) and s[i] == s[i - k]:
#                     i += 1
#                 Z[k] = i - k
#
#                 lt = k
#                 rt = i - 1
#     return Z
[0, 2, 1, 0, 0, 0, 5, 2, 1, 0, 0, 0, 0, 0, 3, 5, 2, 1, 0, 0, 0, 2, 1, 0, 0, 1, 0, 0, 3, 3, 3, 5, 2, 1, 0, 0]
[0, 2, 1, 0, 0, 0, 5, 2, 1, 0, 0, 0, 0, 0, 3, 5, 2, 1, 0, 0, 0, 2, 1, 0, 0, 1, 0, 0, 3, 3, 3, 5, 2, 1, 0, 0]
[0, 2, 2, 0, 0, 0, 5, 2, 2, 0, 0, 0, 0, 0, 3, 17, 5, 2, 0, 0, 0, 2, 22, 0, 0, 1, 0, 0, 3, 33, 4, 32, 3, 1, 0, 0]
# [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2]
#         int Z[] = new int[input.length];
#         int left = 0;
#         int right = 0;
#         for(int k = 1; k < input.length; k++) {
#             if(k > right) {
#                 left = right = k;
#                 while(right < input.length && input[right] == input[right - left]) {
#                     right++;
#                 }
#                 Z[k] = right - left;
#                 right--;
#             } else {
#                 //we are operating inside box
#                 int k1 = k - left;
#                 //if value does not stretches till right bound then just copy it.
#                 if(Z[k1] < right - k + 1) {
#                     Z[k] = Z[k1];
#                 } else { //otherwise try to see if there are more matches.
#                     left = k;
#                     while(right < input.length && input[right] == input[right - left]) {
#                         right++;
#                     }
#                     Z[k] = right - left;
#                     right--;
#                 }
#             }
#         }
#         return Z;
#     }
