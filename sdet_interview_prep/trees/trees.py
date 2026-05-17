# =============================================================================
# TOPIC: TREES (Binary Trees & Binary Search Trees)
# =============================================================================
#
# WHAT IS A TREE?
# A tree is a hierarchical data structure with a root node and children.
# Each node has at most one parent and zero or more children.
#
# BINARY TREE: each node has at most 2 children (left and right)
# BINARY SEARCH TREE (BST): left child < node < right child (sorted property)
#
# KEY TERMS:
# - Root: topmost node (no parent)
# - Leaf: node with no children
# - Height: longest path from root to leaf
# - Depth: distance from root to a node
# - Level: all nodes at the same depth
#
# TREE TRAVERSALS (most important to know):
# 1. Inorder   (Left -> Root -> Right)  -> gives sorted order for BST
# 2. Preorder  (Root -> Left -> Right)  -> used to clone/copy a tree
# 3. Postorder (Left -> Right -> Root)  -> used to delete a tree
# 4. Level Order (BFS)                  -> level by level, uses a Queue
#
# HOW TO THINK ABOUT TREE PROBLEMS:
# 1. Can I solve it with DFS (recursion on left and right)?
# 2. Do I need to process level by level? -> use BFS with a Queue
# 3. What information do I need to return from each subtree?
# 4. What's the base case? (node is None)
#
# TIME COMPLEXITIES (Balanced BST):
# Search, Insert, Delete -> O(log n)
# All traversals         -> O(n) — must visit every node
#
# COMMON PATTERNS IN INTERVIEWS:
# - Recursive DFS for height, path sum, diameter
# - BFS (level order) for level-by-level operations
# - Checking BST property
# - Finding LCA (Lowest Common Ancestor)
#
# =============================================================================
# NODE CLASS (Used in all problems below)
# =============================================================================

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    return root


# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Inorder traversal of a binary tree (Left -> Root -> Right)
# Input:  tree above
# Output: [1, 2, 3, 4, 5, 6, 7]

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

print("Q1 - Inorder Traversal:", inorder(build_tree()))


# Q2: Level Order Traversal (BFS) — return nodes level by level
# Input:  tree above
# Output: [[4], [2, 6], [1, 3, 5, 7]]

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

print("Q2 - Level Order Traversal:", level_order(build_tree()))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Find the height (max depth) of a binary tree
# Input:  tree above
# Output: 3

# Q4: Preorder traversal (Root -> Left -> Right)
# Input:  tree above
# Output: [4, 2, 1, 3, 6, 5, 7]

# Q5: Postorder traversal (Left -> Right -> Root)
# Input:  tree above
# Output: [1, 3, 2, 5, 7, 6, 4]

# Q6: Check if a binary tree is a valid BST
# Hint: use min/max bounds as you recurse

# Q7: Find the lowest common ancestor (LCA) of two nodes in a BST
# Input:  BST above, nodes with val=1 and val=3
# Output: node with val=2

# Q8: Count the total number of nodes in a binary tree
# Input:  tree above
# Output: 7

# Q9: Check if two binary trees are identical (same structure and values)
# Hint: recursive — compare root values and recurse on left and right

# Q10: Find the diameter of a binary tree
# (diameter = longest path between any two nodes, may not pass through root)
# Input:  tree above
# Output: 4  (path: 1 -> 2 -> 4 -> 6 -> 7)
