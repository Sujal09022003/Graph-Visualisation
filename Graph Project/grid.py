import random
from point import Point

GRID_SIZE = 50

def generate_random_grid():
    grid = [[0 if random.randint(0, 5) != 0 else 1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    return grid

def get_neighbors(p):
    neighbors = []
    if p.x > 0: neighbors.append(Point(p.x - 1, p.y))
    if p.x < GRID_SIZE - 1: neighbors.append(Point(p.x + 1, p.y))
    if p.y > 0: neighbors.append(Point(p.x, p.y - 1))
    if p.y < GRID_SIZE - 1: neighbors.append(Point(p.x, p.y + 1))
    return neighbors
