#BFS PROGRAM
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': [],
    'C': []
}

visited = set()
queue = deque(['A'])

visited.add('A')

print("BFS Traversal:")
while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

BFS Traversal:
A B C 



#DFS PROGRAM
graph = {
    'A': ['B', 'C'],
    'B': [],
    'C': []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

print("DFS Traversal:")
dfs('A')

DFS Traversal:
A B C 
