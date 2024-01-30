from collections import defaultdict

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

graph = defaultdict(list)
def prepare_adjaceny_list(edges):
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

# The following is the dfs based implementation of the hasPath problem.
def has_path_dfs(s, d, visited):
    if s == d:
        return True
    if s in visited:
        return False
    
    visited.add(s)
    
    for neighbour in graph[s]:
        if has_path_dfs(neighbour, d, visited):
            return True
    return False

source = 'i'
destination = 'm'
visited = set()
prepare_adjaceny_list(edges)
print(f'DFS says: {has_path_dfs(source, destination, visited)}')