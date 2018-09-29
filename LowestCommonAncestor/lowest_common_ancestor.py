# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import Queue


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        pq_val = [p.val, q.val]
        pq_in_tree = []
        q = Queue.Queue()
        fathers = {}
        q.put((root, 0))
        pq_level = {}
        while len(pq_val):
            temp = q.get()
            node = temp[0]
            node_val = node.val
            level = temp[1]
            if node_val in pq_val:
                pq_val.remove(node_val)
                pq_in_tree.append((node, level))
            for x in (node.left, node.right):
                if x is not None:
                    q.put((x, level + 1))
                    fathers[x] = node

        p, level_p, q, level_q = pq_in_tree[0][0], pq_in_tree[0][1], pq_in_tree[1][0], pq_in_tree[1][1]
        diff = abs(level_p - level_q)
        if level_p < level_q:
            low, high = q, p
        else:
            low, high = p, q
        while diff > 0:
            father = fathers[low]
            low = father
            diff -= 1
        if low == high:
            return low
        else:
            while low != high:
                low, high = fathers[low], fathers[high]
            return low


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = TreeNode(2)
q = TreeNode(4)

S = Solution()
print S.lowestCommonAncestor(root,p,q).val