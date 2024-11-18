"""
Author(s): 1. Hanzala B. Rehan
Description: A script to display a 2D grid represented as a list of characters using pygame, implemented as a class.
Date created: November 15th, 2024
Date last modified: November 15th, 2024
"""

import pygame


class GridDisplay:
    """
    Desc: Class to handle the display of a 2D grid using pygame.
    """

    TILE_SIZE = 40  # Size of each grid tile
    PADDING = 40    # Padding around the grid

    # Colors
    COLOR_WALL = (30, 30, 30)           # Black for walls
    COLOR_PATH = (244, 246, 255)        # White for paths
    COLOR_START = (235, 45, 45)         # Red for start
    COLOR_GOAL = (79, 174, 31)          # Green for goal
    COLOR_BG = (0, 0, 0)                # Black background
    COLOR_BORDER = (0, 0, 0)            # Black border for tiles
    COLOR_EXPLORED = (210, 80, 73)      # Light Red for explored tiles
    COLOR_PATH_TILE = (218, 240, 100)   # Yellow for path tiles

    def __init__(self, grid):
        """
        Desc: Initializes the GridDisplay class.
        Parameters:
            grid (list of list of str): 2D grid representation.
        """
        self.grid = grid
        self.grid_width = len(grid[0])
        self.grid_height = len(grid)
        self.screen_width = (self.grid_width * self.TILE_SIZE) + 2 * self.PADDING
        self.screen_height = (self.grid_height * self.TILE_SIZE) + 2 * self.PADDING

        # Initialize pygame and set up display
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2D Grid Display")

    def draw_grid(self):
        """
        Desc: Draw the grid on the screen based on the predefined grid.
        returns:
        None
        """
        # Draw padding (background)
        self.screen.fill(self.COLOR_BG)

        for row in range(self.grid_height):
            for col in range(self.grid_width):
                rect = pygame.Rect(
                    self.PADDING + col * self.TILE_SIZE,
                    self.PADDING + row * self.TILE_SIZE,
                    self.TILE_SIZE,
                    self.TILE_SIZE
                )
                if self.grid[row][col] == '#':
                    pygame.draw.rect(self.screen, self.COLOR_WALL, rect)
                elif self.grid[row][col] == ' ':
                    pygame.draw.rect(self.screen, self.COLOR_PATH, rect)
                elif self.grid[row][col] == 'S':
                    pygame.draw.rect(self.screen, self.COLOR_START, rect)
                elif self.grid[row][col] == 'G':
                    pygame.draw.rect(self.screen, self.COLOR_GOAL, rect)

                pygame.draw.rect(self.screen, self.COLOR_BORDER, rect, 1)

    def explore(self, x, y):
        """
        Desc: Change the color of a specific tile (x, y) to indicate it has been explored.
        Parameters:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
        returns:
            None
        """
        rect = pygame.Rect(
            self.PADDING + x * self.TILE_SIZE,
            self.PADDING + y * self.TILE_SIZE,
            self.TILE_SIZE,
            self.TILE_SIZE
        )
        # Change the color of the tile to blue for explored
        pygame.draw.rect(self.screen, self.COLOR_EXPLORED, rect)
        pygame.draw.rect(self.screen, self.COLOR_BORDER, rect, 1)

    def draw_path(self, path):
        """
        Desc: Change the color of all tiles in the given path to indicate the path.
        Parameters:
            path (list of tuple): A list of (x, y) coordinates representing the path.
        returns:
            None
        """
        for (x, y) in path:
            rect = pygame.Rect(
                self.PADDING + x * self.TILE_SIZE,
                self.PADDING + y * self.TILE_SIZE,
                self.TILE_SIZE,
                self.TILE_SIZE
            )
            # Change the color of the tile to yellow for path
            pygame.draw.rect(self.screen, self.COLOR_PATH_TILE, rect)
            pygame.draw.rect(self.screen, self.COLOR_BORDER, rect, 1)

    def run(self):
        """
        Desc: Runs the pygame loop to display the grid.
        returns:
        None
        """
        running = True
        clock = pygame.time.Clock()

        while running:
            self.draw_grid()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    # Example grid
    grid = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', 'G', ' '],
        ['#', ' ', '#', '#', '#', '#', '#', ' '],
        ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
        ['#', '#', '#', ' ', '#', ' ', '#', ' '],
        ['#', ' ', ' ', 'S', ' ', ' ', ' ', ' '],
        ['#', '#', '#', '#', '#', '#', '#', '#']
    ]

    display = GridDisplay(grid)
    display.run()
