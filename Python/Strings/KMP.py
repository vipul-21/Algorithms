def KMP(str,p):
    def preprocess_pattern(p):
        i = 0
        j = 1
        s = [0]
        while j < len(p):
            if p[i] == p[j]:
                s.append(i+1)
                i+=1
                j+=1
            else:
                if i != 0:
                    i = s[i-1]
                else:
                    s.append(0)
                    j+=1
        return s
    pre = preprocess_pattern(p)
    i = 0
    j = 0
    while i < len(str):
        print(i,j, len(p))

        if str[i] == p[j]:
            i+=1
            j+=1
            if j == len(p):
                return True
        else:
            if j != 0:
                j = pre[j-1]
            else:
                i+=1
    return False
    
print(KMP('aaabaacbaab', 'aabg'))
# 0 0 0 1 2 0
