import collections
def RabinKarp(s,p):
    if len(p) == 0:
        return True
    i = 0
    j = len(p)
    d = collections.defaultdict(bool)
    # print(rollingHash(s,p))
    while j < len(s):
        d[s[i:j]] = True
        if p in d:
            return True
        j+=1
        i+=1
    return False

prime = 101
def rollingHash(s, p):
    d = collections.defaultdict(list)
    i = 0
    j = len(p)
    def calculateHash(str, index):
        su = 0
        for val in str:
            su += ord(val)*pow(prime, index)
            index+=1
        return su
    while j < len(s):
        d[calculateHash(s[i:j], i)].append(s[i:j])
        j+=1
        i+=1
    return d

# print(RabinKarp('abcdafdas','afs'))
