# Binary Trees

- 

🦋 Basic Structure

         (A)
        /   \
    _______
  __| (B) |  (C)
 |    / \ |___
 |  (D)  (E)  |
 | /  ________|  -> `subtree`: smaller tree
 |(F) |
 |____|

- Nodes(), items (letters), and links / \
    - Node has parent pointer, left and right child
                        parent (prev)
                      /
                    (A)
            left    / \     right (next)
            child (B)  (C)  child
    - No parent? root node
    - No child? left node
    - Node      (A) (B) (C)
    - item       A   B   C
    - parent     /  (A) (A)
    - left      (B)  /   /
    - right     (C)  /   /

- `Depth` (downward): # of links in a path
    - E.g. from A to D: 2

- `Height` (upward): # of edges/inks in longest downward path
    - E.g. from A to F: 3

# Traversal
- Going through a tree by visiting each node, one at a time

# Balanced Binary Tree
- The left and right sides of every node are close in height - no side is more than 1 higher
    🦋 Balanced             🦋 Unbalanced
            1                           1
           / \                         /
          2   3                       2
         /                           /
        4                           3
    
    🦋 Checking if a binary tree is balanced
    def check(node):
        👉 if there aren't any nodes (empty tree)
        if not node:
            return 0

        👉 compute height of right/left subtrees
        left = check(node.left) 
        right = check(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1