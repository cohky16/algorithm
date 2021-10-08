def tree_by_levels(node):
    if not node: return []
    q = [node]
    r = []
    while (len(q) > 0):
        p = q.pop(0)
        r.append(p.value)
        if p.left: q.append(p.left)
        if p.right: q.append(p.right)
    return r