# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        curr_nodes = [root]
        new_nodes = []

        ret = []
        last_val = 0
        curr_val = 0

        while curr_nodes:
            for n in curr_nodes:
                curr_val += 1
                if n:
                    last_val = curr_val
                    ret.append(str(n.val))
                    new_nodes.append(n.left)
                    new_nodes.append(n.right)
                else:
                    ret.append("n")

            curr_nodes = new_nodes
            new_nodes = []

        ret_s = ','.join(ret[:last_val])
        print(ret_s)
        return ret_s


    def deserialize(self, data):
        if not data:
            return

        root = None
        s = []

        for i, n in enumerate(data.split(",")):
            node = TreeNode(int(n)) if n != "n" else None
            if not root:
                root = node

            if s:
                _s = s[0]
                if i % 2 == 1:
                    _s.left = node
                if i % 2 == 0:
                    _s.right = node
                    s.pop(0)

            if node:
                s.append(node)

        return root
