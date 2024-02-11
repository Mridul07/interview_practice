graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['9'],
  '4' : ['8'],
  '8' : [],
  '1' : [],
  '9' : []
}

visited = set()

def connected_components(graph, visited):
    count = 0
    for node in graph:
        if(explore(graph, node, visited) == True):
            count += 1
    
    return count

def explore(graph, curr, visited):
    if curr in visited:
        return False
    visited.add(curr)

    for neighbour in graph[curr]:
        explore(graph, neighbour, visited)
    
    return True

print(f'The connected components for the defined graph is: {connected_components(graph, visited)}')