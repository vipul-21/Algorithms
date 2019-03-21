def dfs(node: 'ListNode', level: 'List[List[int]]') -> 'int':
    if node == None:
        return
    else:
        dfs(node.left, level)
        level.append([node.val])
        dfs(node.right, level)
    return level
