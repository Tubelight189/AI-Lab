# A* Arnav Adarsh 2305199
import heapqa
def astar(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f_cost, node)
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {}
    while open_list:
        current_f, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]

        # Explore neighbors
        for neighbor, weight in graph[current]:
            temp_g = g_cost[current] + weight

            if temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f_cost = temp_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    return None
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

result = astar(graph, heuristic, start, goal)

if result:
    path, cost = result
    print("Shortest Path:", path)
    print("Total Cost:", cost)
else:
    print("No path found")
