class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        q = [] # maintains DFS traversal
        paths = [] # maintains node ordering
        visited_nodes = {}

        q.append(root)
        while True:
            if len(q) == 0:
                break

            node = q.pop(0)
            if node == None:
                paths.append(None)
                continue

            if str(node) not in visited_nodes:
                visited_nodes[str(node)] = True

                paths.append(node.val)

                if node.left != None:
                    q.append(node.left)
                else:
                    q.append(None)
                if node.right != None:
                    q.append(node.right)
                else:
                    q.append(None)


        agg_paths(paths)
        max = get_max_path(paths)
        return max

def get_nodes(l):
    nodes = []
    for i, v in enumerate(l):
        if v == None:
            continue
        node = TreeNode(v)
        nodes.append(node)
        parent = get_parent(i)
        if parent != None:
            if is_left_child(i):
                nodes[parent].left = node
            else:
                nodes[parent].right = node
    return nodes

def agg_paths(paths):
    for i in reversed(range(len(paths))):
        parent = get_parent(i)

        if parent != None:
            if paths[i] != None and paths[i] > 0:
                paths[parent] = paths[parent] + paths[i]

def is_left_child(i):
    return i % 2 == 1

def is_right_child(i):
    return i % 2 == 0

def get_parent(i):
    if is_left_child(i):
        parent = int((i - 1) / 2)
    elif is_right_child(i):
        parent = int((i - 2) / 2)

    return parent if parent >= 0 else None

nodes = get_nodes([-10,9,20,None,None,15,7])
assert(nodes[0].val == -10)
assert(nodes[0].left.val == 9)
assert(nodes[0].right.val == 20)

assert(get_parent(0) == None)
assert(get_parent(1) == 0)
assert(get_parent(2) == 0)
assert(get_parent(3) == 1)
assert(get_parent(4) == 1)
