# Define the game tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values for the terminal nodes
heuristic_values = {
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}

# Alpha-Beta Pruning algorithm
def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    # Base case: if node is terminal or depth is 0
    if depth == 0 or not tree[node]:
        return heuristic_values.get(node, 0)

    if maximizingPlayer:
        value = float('-inf')
        for child in tree[node]:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cut-off
        return value
    else:
        value = float('inf')
        for child in tree[node]:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cut-off
        return value

# Run the algorithm from the root node
result = alpha_beta('A', depth=3, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True)
print("Best value for root node A:", result)

