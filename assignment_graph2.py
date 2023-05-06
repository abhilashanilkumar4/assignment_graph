from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def count_nodes_at_level(root, level):
    if not root:
        return 0

    queue = deque([(root, 0)])
    count = 0

    while queue:
        node, node_level = queue.popleft()

        if node_level == level:
            count += 1

        for child in node.children:
            queue.append((child, node_level + 1))

    return count
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def count_nodes_at_level(root, level):
    if not root:
        return 0

    queue = deque([(root, 0)])
    count = 0

    while queue:
        node, node_level = queue.popleft()

        if node_level == level:
            count += 1

        for child in node.children:
            queue.append((child, node_level + 1))

    return count

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root.children = [node2, node3]
node2.children = [node4, node5, node6]

level = 1
count = count_nodes_at_level(root, level)
print(f"Number of nodes at level {level}: {count}")
