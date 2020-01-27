# There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such
# that there are no gaps between any of them, while keeping overall movement to a minimum.
def minimumJumps(arr):
    people = []
    for i,val in enumerate(arr):
        if val == 1:
            people.append(i)

    if len(people) == 0:
        return 0
    ans = 0
    curr = 1
    median = len(people) // 2
    for i in range(0, median):
        ans += people[median] - people[i] - curr
        curr += 1
    curr = 1
    for i in range(median+1, len(people)):
        ans += people[i] - people[median] - curr
        curr += 1
    return ans

arr = [0, 1, 1, 0, 1, 0, 0, 0, 1]
print(minimumJumps(arr))
