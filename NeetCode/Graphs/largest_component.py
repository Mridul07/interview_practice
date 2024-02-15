graph = {
  '0' : ['8','1', '5', '2'],
  '1' : ['0'],
  '5' : ['0', '8'],
  '8' : ['0', '5'],
  '2' : ['3', '4', '8'],
  '3' : ['2', '4'],
  '4' : ['3', '2']
}

def largestComponent(graph):

    visited = set()
    longest = 0

    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size
    
    return longest

def exploreSize(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    
    size = 1
    for neighbour in graph[node]:
        size += exploreSize(graph, neighbour, visited)
    
    return size


print(largestComponent(graph))