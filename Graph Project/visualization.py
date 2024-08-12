import pygame
from grid import GRID_SIZE, generate_random_grid
from point import Point
from algorithms import dfs, bfs, dijkstra, bellman_ford, a_star

CELL_SIZE = 10
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

def visualize_path(grid, path, screen, color):
    for p in path:
        pygame.draw.rect(screen, color, (p.x * CELL_SIZE, p.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_legend(screen):
    font = pygame.font.Font(None, 24)
    legend_texts = [
        ("DFS", (255, 0, 0)),
        ("BFS", (0, 255, 0)),
        ("Dijkstra", (0, 0, 255)),
        ("Bellman-Ford", (255, 255, 0)),
        ("A*", (255, 0, 255)),
    ]
    for i, (text, color) in enumerate(legend_texts):
        label = font.render(text, True, color)
        screen.blit(label, (10, 10 + i * 20))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Pathfinding Visualization')

    grid = generate_random_grid()
    start = end = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                point = Point(x // CELL_SIZE, y // CELL_SIZE)
                if not start:
                    start = point
                elif not end:
                    end = point

        screen.fill((255, 255, 255))

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                color = (0, 0, 0) if grid[x][y] == 1 else (255, 255, 255)
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if start:
            pygame.draw.rect(screen, (0, 255, 255), (start.x * CELL_SIZE, start.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        if end:
            pygame.draw.rect(screen, (255, 165, 0), (end.x * CELL_SIZE, end.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        draw_legend(screen)
        pygame.display.flip()

        if start and end:
            if grid[start.x][start.y] == 1 or grid[end.x][end.y] == 1:
                print("Start or end point is an obstacle. Exiting.")
                break

            dfs_path = dfs(grid, start, end)
            bfs_path = bfs(grid, start, end)
            dijkstra_path = dijkstra(grid, start, end)
            bellman_ford_path = bellman_ford(grid, start, end)
            a_star_path = a_star(grid, start, end)

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                screen.fill((255, 255, 255))

                for x in range(GRID_SIZE):
                    for y in range(GRID_SIZE):
                        color = (0, 0, 0) if grid[x][y] == 1 else (255, 255, 255)
                        pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                visualize_path(grid, dfs_path, screen, (255, 0, 0))
                visualize_path(grid, bfs_path, screen, (0, 255, 0))
                visualize_path(grid, dijkstra_path, screen, (0, 0, 255))
                visualize_path(grid, bellman_ford_path, screen, (255, 255, 0))
                visualize_path(grid, a_star_path, screen, (255, 0, 255))

                draw_legend(screen)
                pygame.display.flip()

            break

    pygame.quit()

if __name__ == "__main__":
    main()
