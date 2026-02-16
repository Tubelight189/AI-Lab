# ucs Arnav Adarsh 2305199
import heapq
def uniform_cost_search(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (cost, node)
    cost_so_far = {node: float('inf') for node in graph}
    cost_so_far[start] = 0
    parent = {}

    while open_list:
        current_cost, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, cost_so_far[goal]
        for neighbor, weight in graph[current]:
            new_cost = cost_so_far[current] + weight

            if new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(open_list, (new_cost, neighbor))
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

start = 'A'
goal = 'G'

result = uniform_cost_search(graph, start, goal)

if result:
    path, cost = result
    print("Shortest Path:", path)
    print("Total Cost:", cost)
else:
    print("No path found")
