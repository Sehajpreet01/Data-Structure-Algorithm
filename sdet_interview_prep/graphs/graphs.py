# =============================================================================
# TOPIC: GRAPHS (BFS and DFS)
# =============================================================================
#
# WHAT IS A GRAPH?
# A graph is a collection of nodes (vertices) connected by edges.
# Unlike trees, graphs can have cycles and multiple paths between nodes.
#
# TYPES OF GRAPHS:
# - Directed: edges have direction (A -> B, but not B -> A)
# - Undirected: edges go both ways (A -- B means A -> B and B -> A)
# - Weighted: edges have costs/distances
# - Unweighted: all edges are equal
# - Cyclic: contains at least one cycle
# - Acyclic: no cycles (DAG = Directed Acyclic Graph)
#
# HOW TO REPRESENT A GRAPH IN CODE:
# Adjacency List (most common in interviews):
#   graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A'],
#     'D': ['B']
#   }
#
# TWO MAIN TRAVERSAL ALGORITHMS:
#
# BFS (Breadth-First Search):
# - Uses a QUEUE
# - Visits all neighbors before going deeper
# - Best for: shortest path, level-by-level exploration
# - Template: start -> add to queue -> while queue: pop, process, add unvisited neighbors
#
# DFS (Depth-First Search):
# - Uses RECURSION or a STACK
# - Goes as deep as possible before backtracking
# - Best for: cycle detection, connected components, topological sort
# - Template: visit node -> mark visited -> recurse on unvisited neighbors
#
# VISITED SET — CRITICAL:
# Always maintain a visited set to avoid infinite loops in cyclic graphs!
#
# TIME COMPLEXITY:
# BFS and DFS both: O(V + E) where V = vertices, E = edges
#
# SDET RELEVANCE:
# - Dependency graphs (test suite dependencies)
# - Network reachability testing
# - Detecting circular dependencies in test setups
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

from collections import deque

# Sample graph (undirected)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Q1: BFS traversal starting from a given node
# Input:  graph above, start = 'A'
# Output: ['A', 'B', 'C', 'D', 'E', 'F']

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

print("Q1 - BFS from A:", bfs(graph, 'A'))


# Q2: DFS traversal starting from a given node (recursive)
# Input:  graph above, start = 'A'
# Output: ['A', 'B', 'D', 'E', 'F', 'C']  (order may vary)

def dfs(graph, node, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(node)
    result.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result

print("Q2 - DFS from A:", dfs(graph, 'A'))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Check if a path exists between two nodes in a graph
# Input:  graph above, src = 'A', dest = 'F'
# Output: True

# Q4: Count the number of connected components in an undirected graph
# Input:  graph = {0:[1,2], 1:[0], 2:[0], 3:[4], 4:[3], 5:[]}
# Output: 3  (components: {0,1,2}, {3,4}, {5})

# Q5: Detect a cycle in an undirected graph
# Input:  a graph with a cycle (like the sample above)
# Output: True

# Q6: Find the shortest path between two nodes (BFS gives shortest in unweighted graph)
# Input:  graph above, src = 'A', dest = 'F'
# Output: ['A', 'C', 'F']  (length 2)

# Q7: Check if a directed graph has a cycle (use DFS with recursion stack)
# Input:  directed_graph = {0:[1], 1:[2], 2:[0]}  (cycle: 0->1->2->0)
# Output: True

# Q8: Topological sort of a DAG (Directed Acyclic Graph)
# Input:  {0:[1,2], 1:[3], 2:[3], 3:[]}  (task dependencies)
# Output: [0, 1, 2, 3] or [0, 2, 1, 3]  (any valid order)

# Q9: Find all nodes reachable from a given source
# Input:  graph above, start = 'D'
# Output: {'D', 'B', 'A', 'C', 'E', 'F'}

# Q10: Given a grid of 0s and 1s, count the number of islands
# (island = connected group of 1s, connected horizontally/vertically)
# Input:  [
#            [1, 1, 0, 0, 0],
#            [1, 1, 0, 0, 0],
#            [0, 0, 1, 0, 0],
#            [0, 0, 0, 1, 1]
#         ]
# Output: 3
