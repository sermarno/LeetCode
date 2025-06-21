# Concepts Covered

- Custom Data Structures Provided
- Recursion

### Key:
- ❣️ Inner Concept
- 🦋 Example
- 👉 Comment
- ✅ Output


## Custom Data Structures Provided
- Most coding platforms will give you a custom data structure to solve the problem, making you use the definition because:
    1. It's how the input is provided and processed
    2. Allows you to interact with .val and .next as a linked list structure
    3. Can't use Python's built-in list methods (e.g. slicing or indexing)

    🦋 def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        - head: start of a chain of nodes
        - each node has a .val (value) and .next (next node)
        - job is to flip all .next pointers

    🦋 Binary Tree Traversal: return the inorder traversal
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        class Solution:
            def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
                result = []
                def dfs(node):
                    if node:
                        dfs(node.left)
                        result.append(node.val)
                        dfs(node.right)
                    dfs(root)
                return result

## Recursion
- A function calls itself to solve smaller versions of a problem until it reaches a base case

    🦋 Factorial
    def factorial(n):
        if n == 0:
            return 1 👉 base case
        return n * factorial(n - 1) 👉 recursive case