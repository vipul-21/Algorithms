def bfs(node: 'ListNode', level: 'List[List[int]]', depth: 'int') -> 'int':
    if node == None:
        return
    else:
        if len(level) <= depth:
            level.append([node.val])
        else:
            level[depth].extend([node.val])
        bfs(node.left, level, depth + 1 )
        bfs(node.right, level, depth + 1)
    return level
