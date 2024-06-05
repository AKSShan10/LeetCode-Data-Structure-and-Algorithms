def dfs_tree_from_adjacency_matrix(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    tree = {}

    def dfs(node, parent=None):
        visited[node] = True
        if parent is not None:
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(node)
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor, node)

    # Assuming we start the DFS from node 0
    dfs(0)
    return tree

# Example usage
adj_matrix = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

tree = dfs_tree_from_adjacency_matrix(adj_matrix)
print(tree)
