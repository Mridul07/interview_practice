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

queue = []
visited = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(f'{m} ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Printing the BFS traversal of the graph declared above")
bfs(visited, graph, '5')