class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __hash__(self):
        return hash((self.x, self.y))

class Node:
    def __init__(self, point, cost, parent=None):
        self.point = point
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

class AStarNode(Node):
    def __init__(self, point, g, h, parent=None):
        super().__init__(point, g + h, parent)
        self.g = g
        self.h = h
