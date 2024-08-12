from point import Point, Node, AStarNode
from grid import get_neighbors, GRID_SIZE

INF = float('inf')
GRID_SIZE = 50

def dfs(grid, start, end):
    stack = [start]
    came_from = {}
    visited = set([start])
    
    while stack:
        current = stack.pop()
        if current == end:
            return reconstruct_path(came_from, start, end)
        
        for neighbor in get_neighbors(current):
            if grid[neighbor.x][neighbor.y] == 0 and neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current
    return []

def bfs(grid, start, end):
    from queue import Queue
    queue = Queue()
    queue.put(start)
    came_from = {}
    visited = set([start])
    
    while not queue.empty():
        current = queue.get()
        if current == end:
            return reconstruct_path(came_from, start, end)
        
        for neighbor in get_neighbors(current):
            if grid[neighbor.x][neighbor.y] == 0 and neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current
    return []

def dijkstra(grid, start, end):
    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put(Node(start, 0))
    cost = {Point(x, y): INF for x in range(GRID_SIZE) for y in range(GRID_SIZE)}
    cost[start] = 0
    came_from = {}
    
    while not pq.empty():
        current = pq.get().point
        
        if current == end:
            return reconstruct_path(came_from, start, end)
        
        for neighbor in get_neighbors(current):
            if grid[neighbor.x][neighbor.y] == 0:
                new_cost = cost[current] + 1
                if new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    pq.put(Node(neighbor, new_cost))
                    came_from[neighbor] = current
    return []

def bellman_ford(grid, start, end):
    cost = {Point(x, y): INF for x in range(GRID_SIZE) for y in range(GRID_SIZE)}
    cost[start] = 0
    came_from = {}
    
    for _ in range(GRID_SIZE * GRID_SIZE - 1):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                current = Point(x, y)
                if cost[current] == INF: continue
                for neighbor in get_neighbors(current):
                    if grid[neighbor.x][neighbor.y] == 0:
                        new_cost = cost[current] + 1
                        if new_cost < cost[neighbor]:
                            cost[neighbor] = new_cost
                            came_from[neighbor] = current
    
    if cost[end] == INF:
        return []
    return reconstruct_path(came_from, start, end)

def a_star(grid, start, end):
    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put(AStarNode(start, 0, heuristic(start, end)))
    g_score = {Point(x, y): INF for x in range(GRID_SIZE) for y in range(GRID_SIZE)}
    g_score[start] = 0
    came_from = {}
    
    while not pq.empty():
        current = pq.get().point
        
        if current == end:
            return reconstruct_path(came_from, start, end)
        
        for neighbor in get_neighbors(current):
            if grid[neighbor.x][neighbor.y] == 0:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, end)
                    pq.put(AStarNode(neighbor, tentative_g_score, heuristic(neighbor, end)))
                    came_from[neighbor] = current
    return []

def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def reconstruct_path(came_from, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
