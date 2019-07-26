def generate(n):
    ans = []
    def recur(curr, open, close, target):
        if close == target:
            ans.append(curr)
        if open > close:
            recur(curr+'}', open, close+1, target)
        if open < n:
            recur(curr+'{', open+1, close, target)
    recur('', 0, 0, n)
    return ans
# print(generate(3))
