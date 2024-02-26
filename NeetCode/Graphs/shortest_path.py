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


def find_shortest_path(graph, start, end):
    visited = set()
    queue = [[start, 0]]
    visited.add(start)

    while(queue):
        currentEdge, dist = queue.pop(0)
        if currentEdge == end:
            return dist
        
        for neighbour in graph[currentEdge]:
            if neighbour[0] not in visited:
                visited.add(neighbour[0])
                queue.append([neighbour, dist + 1])


source = 'o'
destination = 'n'
prepare_adjaceny_list(edges)
print(f'Shortest Path Length: {find_shortest_path(graph, source, destination)}')