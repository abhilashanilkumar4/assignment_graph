class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def count_trees(forest):
    root_vals = set()
    child_vals = set()
    
    for tree in forest:
        root_vals.add(tree.val)
        for child in tree.children:
            child_vals.add(child.val)
    
    return len(root_vals - child_vals)

root1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
root1.children = [node2, node3]
root4 = TreeNode(4)
node5 = TreeNode(5)
root4.children = [node5]
root6 = TreeNode(6)
forest = [root1, root4, root6]

num_trees = count_trees(forest)
print(f"Number of trees in the forest: {num_trees}")
