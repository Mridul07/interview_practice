graph = {
  '5' : ['3','7', '1'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['9'],
  '4' : ['8'],
  '8' : [],
  '1' : [],
  '9' : []
}

# The following is the bfs based implementation of the hasPath problem.
queue = []
def has_path_bfs(graph, s, d):
    queue.append(s)
    while queue:
        curr = queue.pop(0)
        if curr == d: 
            return True
        for neighbour in graph[curr]:
            queue.append(neighbour)
    
    return False


# The following is the dfs based implementation of the hasPath problem.
def has_path_dfs(graph, s, d):
    if s == d:
        return True
    
    for neighbour in graph[s]:
        if has_path_dfs(graph, neighbour, d):
            return True
    return False

source = '5'
destination = '9'
print(f'BFS says: {has_path_bfs(graph, source, destination)}')
print(f'DFS says: {has_path_dfs(graph, source, destination)}')