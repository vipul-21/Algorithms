def videoStitching(clips, T):
        # clips.sort(key = lambda x:(x[0], x[1]))
        n = len(clips)
        ans = [float('inf')]*(T+1)
        for j in range(T+1):
            for i in range(n):
                if j >= clips[i][0] and j <= clips[i][1]:
                    if clips[i][0] == 0:
                        ans[j] = 1
                    else:
                        ans[j] = min(ans[j],1+ans[clips[i][0]])

        return ans[-1] if ans[-1] != float('inf') else -1
# [[0,5],[6,8]]
# 7
# [[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]]
# 5
# [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
# 10
# [[0,1],[1,2]]
# 5
# [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
# 9
# [[0,4],[2,8]]
# 5
print(videoStitching([[0,4],[2,8]],5))
# -1
# 1
# 3
# -1
# 3
# 2
