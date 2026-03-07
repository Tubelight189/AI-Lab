#ARNAV ADARSH 2305199
from collections import deque
def bfs(graph, start, end):
    if start == end:return [start]
    startQueue = deque([start])
    endQueue = deque([end])
    startVisited = {start: None}
    endVisited = {end: None}
    while startQueue and endQueue:
        startNode = startQueue.popleft()
        for node in graph[startNode]:
            if node not in startVisited:
                startVisited[node] = startNode
                startQueue.append(node)
                if node in endVisited:return build_path(node, startVisited, endVisited)
        endNode = endQueue.popleft()
        for node in graph[endNode]:
            if node not in endVisited:
                endVisited[node] = endNode
                endQueue.append(node)
                if node in startVisited:return build_path(node, startVisited, endVisited)
    return None

def build_path(meet, startVisited, endVisited):
    path_start = []
    node = meet
    while node is not None:
        path_start.append(node)
        node = startVisited[node]
    path_start.reverse()
    path_end = []
    node = endVisited[meet]
    while node is not None:
        path_end.append(node)
        node = endVisited[node]
    return path_start + path_end

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F']
}
print(bfs(graph, 'A', 'E'))
print(bfs(graph, 'A', 'F'))
