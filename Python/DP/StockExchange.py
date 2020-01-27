def stack_exchange(arr):
    if len(arr) <=1:
        return None
    curr = arr[0]
    ma = 0
    for i, val in enumerate(arr):
        ma = max(max, val - curr)
        curr = min(curr, val)
    return ma

#Input is the list of values of stack exchanges
#stack_exchange([2,3,4,1,2,6,8])
