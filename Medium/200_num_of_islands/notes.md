# CONCEPTS COVERED
DEPTH-FIRST SEARCH (DFS)
BREADTH-FIRST SEARCH (BFS)
RANGE(LEN())

# DEPTH-FIRST SEARCH (DFS)
- Explores as far down one path as possible before backing up and trying another
- Use cases:
    - Grid/graph traversal
    - Solving mazes
    - Detecting cycles
    - Island counting
    - Backtracking problems (Sudoki, etc.)
- Use recursion or a stack to:
    1. Visit starting node
    2. Move to one neighbor
    3. Then one of its neighbors
    4. And so on...
    5. Backtract where there are no more unvisited neighbors


# BREADTH-FIRST SEARCH (BFS)
- Explores all neighbors of a node first, before going deeper
- Use cases:
    - Finding shortest path
    - Level-order traversal of trees
    - Flood fill
    - Social network connections
- Use a queue:
    1. Start at root
    2. Visit all direct neighbors
    3. Then their neighbors
    4. Then theirs...


# RANGE(LEN())
🦋 Example Grid
    grid = [
    ["1", "0", "1"],
    ["0", "1", "0"],
    ["1", "0", "1"]
    ]

1. len(grid) - gives you the num of rows in 2D grid
    - len(grid) = 3 -> 3 rows
2. range(len(grid)) - gives you a sequence of row indices to loop through
    - range(3)


