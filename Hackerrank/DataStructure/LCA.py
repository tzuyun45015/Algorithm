def LCA(root,v1,v2):
  cur = root
  while cur:
    if v1 < cur.info and v2 < cur.info:
      cur = cur.left
    elif v1 > cur.info and v2 > cur.info:
      cur = cur.right
    else:
      return cur
