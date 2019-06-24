class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def get_max(p):
    a = sum(p)
    b = p[0] + p[2]
    c = p[1] + p[2]
    d = p[2]
    m = max(a,b,c,d)

    return m

def get_max_path(paths):
    print(paths)
    mm = sum(paths[0])
    for p in paths:
        m = get_max(p)
        if m > mm:
            mm = m

    return mm

def update_parent(paths, node):
    curr_node = node
    local_max = node.val
    while True:
        m = get_max(paths[curr_node.index])
        if m > local_max:
            local_max = m
        if m <= 0:
            return local_max
        if curr_node.parent != None:
            my_vals = paths[curr_node.index]
            max_1_chain = max(my_vals[:2]) + curr_node.val

            if curr_node.parent.left == curr_node:
                p_i = 0
            else:
                p_i = 1

            paths[curr_node.parent.index][p_i] = max_1_chain
            curr_node = curr_node.parent
        else:
            break

    return local_max

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max = root.val

        q = [] # maintains DFS traversal
        paths = [] # maintains node ordering
        nodes = []

        q.append(root)
        root.parent = None
        while True:
            if len(q) == 0:
                break

            node = q.pop(0)
            node.index = len(paths)
            paths.append([0,0,node.val])
            nodes.append(node)

            if node.left != None:
                node.left.parent = node
                q.append(node.left)

            if node.right != None:
                node.right.parent = node
                q.append(node.right)

        for node in nodes:
            m = update_parent(paths, node)
            if m > max:
                max = m

        return max

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def maxPathSumHelper(line):
    root = stringToTreeNode(line)
    return Solution().maxPathSum(root)


assert(maxPathSumHelper('[-10,9,20,null,null,15,7]') == 42)
assert(maxPathSumHelper('[1,2,3]') == 6)
assert(maxPathSumHelper('[1,2,null,3,null,4,null,5]') == 15)
assert(maxPathSumHelper('[1,-2,-3,1,3,-2,null,-1]') == 3)
assert(maxPathSumHelper('[2,-1,-2]') == 2)
