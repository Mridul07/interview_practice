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

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Printing the DFS traversal of the graph declared above")
dfs(visited, graph, '5')